#!/usr/bin/env python
# -*- coding: utf-8 -*-
import _envi
import hashlib
from model.connect import db, mc

class Kv(object):
    def __init__(self, table_name):
        self.table_name = table_name
        self.prefix = 'mc_%s_%%s' % table_name 

    def set(self, id, value):
        mc_key = self.prefix % id
        db.execute('insert into %s (id, value) VALUES (%%s, %%s) on duplicate key UPDATE value=%%s' % self.table_name, 
            id, value, value)

    def get(self, id):
        mc_key = self.prefix % id
        value = mc.get(mc_key)
        if value is None:
            r = db.get("select value from %s where id=%%s" % self.table_name, id)
            if r:
                value = r.value
                mc.set(mc_key, value)
        return value

    def get_list(self, id_li):
        result = []
        for id in id_li:
            result.append(self.get(id))
        return result

    def id_by_value(self, value):
        _hash = hashlib.md5(value).hexdigest()
        mc_key = self.prefix % _hash
        id = mc.get(mc_key)
        if id is None:
            r = db.get('select id from %s where value=%%s' % self.table_name, value)
            if r:
                id = r.id
                mc.set(mc_key, id)
        return id


    def save(self, value):
        id = db.execute_lastrowid("INSERT INTO %s (value) VALUES (%%s)" % self.table_name, value)
        mc_key = self.prefix % id
        mc.set(mc_key, value)
        return id

    def delete(self, id):
        mc_key = self.prefix % id
        mc.delete(mc_key)
        db.execute("delete from %s where id=%%s" % self.table_name, id)

if __name__ == '__main__':
    pass
    s = Kv('Session')
    #print s.save('asdfg')
    print s.id_by_value('asdfg')
    print s.set(6, 'sbsafqwfqwfb')
    print s.get(6)
