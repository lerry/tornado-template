#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
from lib.route import Route
from view._base import View, NoLoginView, LoginView, AdminView

route = Route("^postcard.lerry.me$")


@route('/')
class Index(View):
    def get(self):
        self.finish('subdomain')
