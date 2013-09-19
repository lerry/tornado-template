#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
import hashlib
from model.db import db
from lib.jsdict import JsDict
from time import time

def _hash_password(password):
    return hashlib.sha1(password).hexdigest()

def user_by_id(user_id):
    return db.get('select * from User where id=%s', user_id)

def user_new(name, password):
    password_hashed = _hash_password(password)
    if not db.get('select id from User where name = %s', name):
        return db.execute_lastrowid('insert into User (name, password) values (%s,%s)', name, password_hashed)

def password_verify(name, password):
    user = db.get('select * from User where name = %s and password= %s ', name, _hash_password(password))
    return user

if __name__ == '__main__':
    pass
    print user_by_id(1)
    print user_new('lerry', 'password')
    print password_verify('lerry', 'password')