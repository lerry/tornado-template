#coding:utf-8
import _envi
#from torndb import Connection
from lerrylib.db_tools import Connection
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB, MEMCACHED_ADDR, DEBUG

if not DEBUG:
    import pylibmc
    mc = pylibmc.Client(MEMCACHED_ADDR)
else:
    from lerrylib.cache import mc
    
db = Connection(MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASSWD, mc=mc)

if __name__ == '__main__':
    pass
