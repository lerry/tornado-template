#coding:utf-8
from torndb import Connection
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB, MEMCACHED_ADDR, DEBUG

import pylibmc
mc = pylibmc.Client(MEMCACHED_ADDR)

db = Connection(MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASSWD)

if __name__ == '__main__':
    pass
