#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
import hashlib
try:
    from ujson import dumps
except ImportError:
    from json import dumps
from time import time
from base64 import b64encode
from random import choice
from lerrylib.highlight import highlight_txt


FUNCTIONS = {
    'dumps': dumps,
    'highlight_txt': highlight_txt,
}

