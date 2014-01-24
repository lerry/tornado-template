#!/usr/bin/python
# -*- coding: utf-8 -*-
class Route(object):
    def __init__(self, domain=None):
        self.handlers = []
        self.domain = domain

    @property
    def subdomain_handlers(self):
        return [self.domain, self.handlers]


    def __call__(self, url):
        def _(cls):
            self.handlers.append((url, cls))
            return cls
        return _