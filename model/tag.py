#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
from model.db import Kv, db, mc

Tag = Kv('Tag')

def tag_new(tag_name):
    tag_name = tag_name.strip()
    id = Tag.id_by_value(tag_name)
    if not id:
        id = Tag.save(tag_name)
    return id

def tag_list(entry_id):
    r_li = db.query("select tag_id from Relationship where entry_id=%s order by id", 
        entry_id)
    id_li = [r.tag_id for r in r_li]
    return Tag.get_list(id_li)

def tag_list_save(entry_id, tag_str):
    tag_li = tag_str.strip().split()
    db.execute('DELETE FROM Relationship WHERE entry_id=%s', entry_id)
    for tag in tag_li:
        tag_id = tag_new(tag)
        db.execute("insert into Relationship(tag_id, entry_id) values(%s, %s)",
            tag_id, entry_id)


def tag_list_by_entry_count():
    r_li = db.query('SELECT tag_id, count(*) as count FROM `Relationship`\
         group by tag_id order by count(*) desc')
    return [[Tag.get(r.tag_id), r.count] for r in r_li]

if __name__ == '__main__':
    print tag_list_save(1, 'python mysql linux')
    print tag_list(1)