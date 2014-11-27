#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pony.orm

to_dict = lambda obj: dict([(i, getattr(obj, i)) for i in obj._adict_.keys()])


def ponyobj_to_dict(obj):
    if obj.__metaclass__ is pony.orm.core.EntityMeta:
        return to_dict(obj)
    if isinstance(obj, pony.orm.core.QueryResult):
        return map(obj, to_dict)
    else:
        return json.JSONEncoder.default(self, obj)

class Encoder(json.JSONEncoder):
    def default(self, obj):
        return ponyobj_to_dict(obj)

_dumps = json.dumps

def dumps(obj):
	return _dumps(obj, cls=Encoder)

json.dumps = dumps
