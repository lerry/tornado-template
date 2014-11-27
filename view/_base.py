#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import json
import tornado.web
#from model.user import user_by_id
#from model.session import session_new, id_by_session, session_rm


class User(object):
    def __init__(self, id):
        self.id = id

    @property
    def is_admin(self):
        return self.id in ADMINS


class View(tornado.web.RequestHandler):
    def prepare(self):
        super(View, self).prepare()
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Credentials', True)
        self.set_header('Access-Control-Allow-Headers', 'accept, content-type')

    def options(self, *arg):
        self.set_header('Access-Control-Allow-Methods', 'PUT, PATCH, DELETE, POST, GET, OPTIONS')
        return self.finish({"test":"ok"})

    def get_json(self):
        return json.loads(self.request.body)

    def finish(self, data=None):
        super(View, self).finish(json.dumps(data))

    @property
    def current_user_id(self):
        s = self.get_secure_cookie('S')
        #return id_by_session(s)
        return 0

    @property
    def current_user(self):
        uid = self.current_user_id
        return User(uid) if uid else None

    def get_number(self, name, default=None):
        v = self.get_argument(name, default)
        if v.isdigit():
            return int(v)

    user = current_user
    uid = current_user_id


class LoginView(View):
    def prepare(self):
        super(LoginView, self).prepare()
        if not self.current_user_id:
            return self.send_error(401)

if __name__ == '__main__':
    s = Session()
    from model.models import Post
    query = s.query(Post)
    for i in query:
        print(i.title)
