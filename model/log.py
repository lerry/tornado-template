#!/usr/bin/python
# -*- coding: utf-8 -*-
from pony.orm import *
from os.path import join
from config import DEBUG, MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASSWD

db = Database("mysql", host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB)

sql_debug(DEBUG)

class Log(db.Entity):
	id = PrimaryKey(int, auto=True)
	source = Required(int)
	create_time = Required(int)
	txt = Optional(unicode)
	author = Optional(int)
	remark = Optional(unicode)

db.generate_mapping(create_tables=False)

@db_session
def fetch(limit, offset):
	return select(i for i in Log).order_by(desc(Log.create_time))[offset:offset+limit]

@db_session
def count():
	return select(i for i in Log).count()


if __name__ == "__main__":
    pass
