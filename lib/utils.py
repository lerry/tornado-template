#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

RE_EMAIL = re.compile(r'^\w+[-+.\w]*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')

class ERR:
    NO_LOGIN = 1
    PERMISSION_DENIED = 2
    OPERATION_FAILED = 3
    POST_TOO_QUICK = 4

