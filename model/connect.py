#coding:utf-8
import _envi
from lib.torndb import Connection
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB, MEMCACHED_ADDR, DEBUG

if not DEBUG:
    import pylibmc
    mc = pylibmc.Client(MEMCACHED_ADDR)
else:
    from lib.cache import cache as mc
    
db = Connection(MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASSWD)

if __name__ == '__main__':
    pass
