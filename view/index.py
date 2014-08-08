#!/usr/bin/python
# -*- coding: utf-8 -*-
from view._route import route
from view._base import View, LoginView

PAGE_LIMIT = 20

@route('/')
class Index(View):
    def get(self):
        self.finish({"name": "lerry"})



if __name__ == '__main__':
    pass
