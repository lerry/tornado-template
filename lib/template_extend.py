#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
import hashlib
try:
    from ujson import dumps
except ImportError:
    from json import dumps
from time import time
from base64 import b64encode
from random import choice
from config.img_list import BG_IMGS
from lerrylib.highlight import highlight_txt

def policy_signature_get(bucket):
    key, host = UPYUN[bucket]
    policy = {
        'bucket'        : bucket,
        'expiration'    : int(time()) + 360000,
        'save-key'      : '/{filemd5}',
    }
    policy = b64encode(dumps(policy))
    signature = hashlib.md5('%s&%s'% (policy, key)).hexdigest()
    return policy, signature

def background_url():
    return 'http://file.lerry.me/nice_pics/%s' % choice(BG_IMGS)

FUNCTIONS = {
    #'upyun': policy_signature_get,
    'dumps': dumps,
    'background_url': background_url,
    'highlight_txt': highlight_txt,
}

