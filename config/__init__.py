#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
from default import *
from getpass import getuser
from os.path import join, dirname, exists

private = join(dirname(__file__), '_private')

if exists(private):
    from config._private import *
    if exists(join(private, '%s.py' % getuser())):
    	exec('from config._private.%s import *' % getuser())

