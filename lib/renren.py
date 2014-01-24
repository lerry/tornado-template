#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from requests import ConnectionError
from lib.jsdict import JsDict
import time, urllib, urllib2, logging, mimetypes, hashlib

class APIError(StandardError):
    '''
    raise APIError if got failed json message.
    '''
    def __init__(self, error_code, error, request):
        self.error_code = error_code
        self.error = error
        self.request = request
        StandardError.__init__(self, error)

    def __str__(self):
        return 'APIError: %s: %s, request: %s' % (self.error_code, self.error, self.request)

def _parse_json(s):
    return JsDict(json.loads(s))

def _encode_params(**kw):
    ' do url-encode parameters '
    args = []
    for k, v in kw.iteritems():
        qv = v.encode('utf-8') if isinstance(v, unicode) else str(v)
        args.append('%s=%s' % (k, urllib.quote(qv)))
    return '&'.join(args)


def _http_post(url, **kw):
    req = requests.post(url, kw, verify=False)
    body = req.text
    r = _parse_json(body)
    if 'error_code' in body:
        raise APIError(r.error_code, r.error, r.request)
    return r



class APIClient(object):
    '''
    API client using synchronized invocation.
    '''
    def __init__(self, app_key, app_secret, redirect_uri=None, response_type='code', domain='renren.com', version='2'):
        self.client_id = app_key
        self.client_secret = app_secret
        self.redirect_uri = redirect_uri
        self.response_type = response_type
        self.auth_url = 'https://graph.%s/oauth/' % domain
        self.api_url = 'https://api.%s/restserver.do' % domain
        self.access_token = None
        self.expires = 0.0

    def set_access_token(self, access_token, expires_in):
        self.access_token = str(access_token)
        self.expires = float(expires_in)

    def get_authorize_url(self, redirect_uri=None, **kw):
        '''
        return the authroize url that should be redirect.
        '''
        redirect = redirect_uri if redirect_uri else self.redirect_uri
        if not redirect:
            raise APIError('21305', 'Parameter absent: redirect_uri', 'OAuth2 request')
        return '%s%s?%s' % (self.auth_url, 'authorize', \
                _encode_params(client_id = self.client_id, \
                        response_type = 'code', \
                        redirect_uri = redirect, **kw))

    def request_access_token(self, code, redirect_uri=None):
        '''
        return access token as object: {"access_token":"your-access-token","expires_in":12345678,"uid":1234}, expires_in is standard unix-epoch-time
        '''
        redirect = redirect_uri if redirect_uri else self.redirect_uri
        if not redirect:
            raise APIError('21305', 'Parameter absent: redirect_uri', 'OAuth2 request')
        r = _http_post('%s%s' % (self.auth_url, 'token'), \
                client_id = self.client_id, \
                client_secret = self.client_secret, \
                redirect_uri = redirect, \
                code = code, grant_type = 'authorization_code')
        return r

    def get_sig(self, api):
        s = 'access_token=%s' % self.access_token + \
        'format=json' + \
        'method=%s' % api +\
        'v=1.0'
        return hashlib.md5(s).hexdigest()

    def api_call(self, api):
        r = _http_post(self.api_url,
                sig = self.get_sig(api),
                access_token = self.access_token,
                format = 'json',
                method = api,
                v = 1.0
                )
        return r

    def is_expires(self):
        return not self.access_token or time.time() > self.expires