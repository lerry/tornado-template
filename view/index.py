#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
import time
from view._route import route
from view._base import View, LoginView, AdminView

PAGE_LIMIT = 20

@route('/')
class Index(View):
    def get(self):
        self.render()



if __name__ == '__main__':
    pass