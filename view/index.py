#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from view._route import route
from view._base import View, LoginView
from tornado.web import StaticFileHandler

@route('/')
class _(View):
    def get(self):
        self.finish({"hello":"world"})

@route('/xxx')
class _(View):
    def get(self):
        self.set_header('Content-Type', 'text/html; charset=UTF-8')
        fp = open("dist/index.html", "rb")
        for chunk in fp.read():
            self.write(chunk)
        self.flush()

if __name__ == '__main__':
    pass
