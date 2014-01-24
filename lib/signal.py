#coding:utf-8
from types import FunctionType

def call(func, args):
    if type(func) is FunctionType:
        args = args[:func.func_code.co_argcount]
    func(*args)

class Signal(object):
    
    def __init__(self, name):
        self._sync = []
        self.name = name 


    def send(self, *args):
        name = self.name
        for func in self._sync:
            call(func,args)

    def __call__(self, func):
        self._sync.append(func)
        return func

class _(object):
    def __getattr__(self, name):
        d = self.__dict__
        if name not in d:
            d[name] = Signal(name)
        return d[name]
        
SIGNAL = _()

if __name__ == "__main__":


    @SIGNAL.follow_new
    def _follow_new(sql):
        print sql
   
    SIGNAL.follow_new.send('select * from sss')

