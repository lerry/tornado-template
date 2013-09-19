#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
import time
from config import HOST
from model.db import db
from config import PAGE_LIMIT, TIME_ZONE, HOST
from lerrylib.highlight import highlight_txt
from model.tag import tag_list, tag_list_save, Tag

def entry_count():
    return db.execute_rowcount('select id from Entry')

def entry_list(limit=PAGE_LIMIT, offset=0):
    li = db.query('select * from Entry order by id desc limit %s offset %s ', limit, offset)
    return map(Entry, li)

class Entry(object):
    def __init__(self, entry):
        self.entry = entry

    def __getattr__(self, name):
        return getattr(self.entry, name)

    @property
    def url(self):
        t = time.strftime('%Y/%m/%d', time.localtime(self.entry.post_time+TIME_ZONE*3600))
        return 'http://%s/post/%s/%s' % (HOST, t, self.entry.slug) 

    @property
    def str_time(self):
        return time.strftime('%Y-%m-%d %H:%M', self._time)

    @property
    def _time(self):
        return time.localtime(self.entry.post_time+TIME_ZONE*3600)

    @property
    def date(self):
        return time.strftime('%Y-%m-%d', self._time)

    @property
    def feed_date(self):
        return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(self.entry.post_time))

    @property
    def html(self):
        txt = self.entry.content
        return highlight_txt(txt)

    @property
    def tag_list(self):
        return tag_list(self.id)

    @property 
    def tag_str(self):
        tag_li = tag_list(self.id)
        return ' '.join(tag_li)

def entry_get(entry_id):
    entry = db.get('select * from Entry where id=%s', entry_id)
    if entry:
        return Entry(entry)

def entry_by_slug(slug):
    entry = db.get('select * from Entry where slug=%s', slug)
    if entry:
        return Entry(entry)

def entry_new(uid, title, slug, txt, tag_str):
    now = int(time.time())
    id = db.execute_lastrowid("insert into Entry(uid, title, slug, content, post_time, update_time) \
        values (%s,%s,%s,%s,%s,%s)", uid, title, slug, txt, now, now)
    tag_list_save(id, tag_str)
    return entry_get(id)


def entry_update(entry_id, title, slug, txt, tag_str):
    now = int(time.time())
    db.execute("update Entry set title=%s, slug=%s, content=%s, update_time=%s where id=%s",\
        title, slug, txt, now, entry_id)
    tag_list_save(entry_id, tag_str)
    return entry_get(entry_id)


def entry_list_by_tag(tag):
    result = []
    tag_id = Tag.id_by_value(tag)
    if tag_id:
        r_li = db.query("select entry_id from Relationship where tag_id=%s order by id", 
            tag_id)
        id_li = [r.entry_id for r in r_li]
        for id in id_li:
            entry = db.get('select * from Entry where id=%s', id)
            result.append(entry)
    return map(Entry, result)


        
if __name__ == '__main__':
    #print entry_by_slug('theFirst')
    print entry_list()