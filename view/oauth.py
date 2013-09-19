#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
import requests
import json
from time import time
from view._route import route
from view._base import View
from config import OAUTH2, HOST
from model.oauth2 import oauth_save

def _encode_params(**kw):
    kw = ['%s=%s' % (k, v) for k, v in kw.iteritems()]
    return  '?' + '&'.join(kw)

@route('/oauth/(\w+)')
class Callback(View):
    def get(self, oauth_type):
        code = self.get_argument('code', '')
        CALLBACK_URL = 'http://%s/oauth/%s' % (HOST, oauth_type)
        url = 'https://www.douban.com/service/auth2/token'
        key, secret = OAUTH2[oauth_type]
        kw = {
            'client_id': key, 
            'client_secret': secret, 
            'redirect_uri': CALLBACK_URL,
            'grant_type': 'authorization_code',
            'code': code
        }

        r = requests.post(url, data=kw)
        data = r.json()
        oauth_id = int(data.get('douban_user_id', 0))
        oauth_save(oauth_id=oauth_id, 
                   oauth_type='douban', 
                   token=data.get('access_token'), 
                   refresh_token=data.get('refresh_token'), 
                   expires_at=int(data.get('expires_in')) + int(time()))
        self.login(oauth_id)
        self.redirect('http://postcard.lerry.me/')




@route('/login/(\w+)')
class Weibo(View):
    def get(self, oauth_type):
        CALLBACK_URL = 'http://%s/oauth/%s' % (HOST, oauth_type)
        key, secret = OAUTH2[oauth_type]
        kw = _encode_params(
            client_id=key,
            redirect_uri=CALLBACK_URL,
            response_type='code'
            )

        url = "https://www.douban.com/service/auth2/auth"+kw
        self.redirect(url)