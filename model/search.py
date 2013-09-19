#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
from model.db import db, Kv
from model.entry import entry_get, Entry
        
def search(q):
    query = '%' + q + '%'
    r = db.query('select * from Entry where title like %s or content like %s order by id desc',\
        query, query)
    return map(Entry, r)



if __name__ == '__main__':
    print search('python')
