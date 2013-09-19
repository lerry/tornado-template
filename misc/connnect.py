#coding:utf-8

# 初始化数据连接
import _envi
import MySQLdb
from DBUtils.SteadyDB import connect
from MySQLdb.converters import FIELD_TYPE, conversions
from lib.cache import cache as mc
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB



class Connection:
    def __init__(self, host, port, user, passwd, db, charset):
        self.conn_params = conn_params = dict(
                host=host, user=user, port=port,
                db=db, init_command='set names %s'%charset,
        )
        if passwd :
            conn_params['passwd'] = passwd
        conv = conversions.copy()
        conv.update({
             FIELD_TYPE.TIMESTAMP: None,
             FIELD_TYPE.DATETIME: None,
             FIELD_TYPE.TIME: None,
             FIELD_TYPE.DATE: None,
        })

        conn_params['conv'] = conv
        conn_params['maxusage'] = False
        self._cursor = None 


    def connect(self):
        conn = connect(MySQLdb, **self.conn_params)

        if not conn:
            raise DatabaseError('can not connect to database: %s %s %s'
                         % (host, user, db))

        cursor = conn.cursor()
        cursor = CursorWrapper(cursor, self)
        return cursor

    def cursor(self):
        if self._cursor is None:
            self._cursor = self.connect()
        return self._cursor


class CursorWrapper(object) :

    def __init__(self, cursor, farm) :
        self._cursor = cursor
        self.farm = farm

    def __getattr__(self, name) :
        return getattr(self._cursor, name)
    
    def __iter__(self):
        return iter(self._cursor)

    def execute(self, *args, **kwargs):
        try:
            return self._execute(*args, **kwargs)
        except:
            self._cursor = self.farm.cursor()
            return self._execute(*args, **kwargs)

    def _execute(self, *args, **kwargs) :
        try :
            return self._cursor.execute(*args, **kwargs)
        except MySQLdb.OperationalError, e:
            error_no = e.args[0]
            if 2000 <= error_no < 3000  :
                self.farm._cursor = None
            self._cursor.connection.rollback()
            raise
        except MySQLdb.ProgrammingError, e:
            if e.args[0] == 2014:
                self.farm._cursor = None
            self._cursor.connection.rollback()
            raise
        except MySQLdb.IntegrityError, e:
            self._cursor.connection.rollback()
            raise


connection = Connection(
    host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB, charset='utf8'
)


if __name__ == "__main__":
    pass