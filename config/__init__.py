#!/usr/bin/python
# -*- coding: utf-8 -*-
from default import *
from os.path import join, dirname, exists

private = join(dirname(__file__), '_private')

if exists(private):
    from config._private import *
