#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
from view._base import route, View

@route('/l')
class Index(View):
    def get(self):
        self.finish('nihao')
