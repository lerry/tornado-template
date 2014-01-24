#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
import uuid
from model.db import Kv

Session = Kv('Session')

def session_new(uid):
    ret = Session.get(uid)
    if ret: return ret
    s = uuid.uuid4().hex
    Session.set(uid, s)
    return s

def id_by_session(s):
    if s:
        return Session.id_by_value(s)

def session_rm(uid):
    #uid = id_by_session(s)
    Session.delete(uid)
        
if __name__ == '__main__':
    pass
    print session_new(123)

