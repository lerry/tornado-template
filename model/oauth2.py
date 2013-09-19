#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
from time import time
from model.db import db, Kv
#oauth_id, oauth_type, token, refresh_token, expires_at


def oauth_get(oauth_id):
    return db.get('select * from Oauth2 where oauth_id = %s', oauth_id)

def oauth_save(**kw):
    if oauth_get(kw['oauth_id']):
        oauth_update(kw)
    else:
        oauth_new(kw)

def oauth_new(kw):
    db.execute('insert into Oauth2(oauth_type, oauth_id, token, refresh_token, expires_at) values(%s, %s, %s, %s, %s)', \
        kw['oauth_type'], kw['oauth_id'], kw['token'], kw['refresh_token'], kw['expires_at'])

def oauth_update(kw):
    db.execute('update Oauth2 set token=%s, refresh_token=%s, expires_at=%s where oauth_id=%s', 
        kw['token'], kw['refresh_token'], kw['expires_at'], kw['oauth_id'])

if __name__ == '__main__':
    pass

