#!/usr/bin/python
# -*- coding: utf-8 -*-
import _envi
import re
import json
import tornado.web
from os.path import join, exists
from lib.utils import ERR
from lib.render import render_jinja
from lib.template_extend import FUNCTIONS
from lib.signal import SIGNAL
from config import ADMINS
#from model.user import user_by_id
#from model.session import session_new, id_by_session, session_rm

TEMPLATE_PATH = join(_envi.PREFIX, 'html')

render = render_jinja(
    TEMPLATE_PATH,
    encoding='utf-8',
)

def logout(self):
    self.clear_cookie('S', domain=self.request.host)
    session_rm(self.current_user_id)

def login(self, uid):
    self.set_secure_cookie('S', session_new(uid), domain=self.request.host, expires_days=999)

@SIGNAL.db_query
def _(sql):
    print sql

class User(object):
    def __init__(self, id):
        self.id = id

    @property
    def is_admin(self):
        return self.id in ADMINS


class View(tornado.web.RequestHandler):
    def prepare(self):
        super(View, self).prepare()
        self.db_query_count = 0   

    @property
    def current_user_id(self):
        s = self.get_secure_cookie('S')
        #return id_by_session(s)
        return 0

    @property
    def current_user(self):
        uid = self.current_user_id
        return User(uid) if uid else None

    user = current_user
    uid = current_user_id

    def render(self, filename=None, **kwargs):
        kwargs['current_user_id'] = self.current_user_id
        kwargs['current_user'] = self.current_user
        _xsrf = self.xsrf_form_html()
        kwargs.update(FUNCTIONS)
        kwargs['_xsrf'] = _xsrf
        kwargs['request'] = self.request
        if not filename:
            filename = '%s/%s.html' % (
                self.__module__[5:].replace('.', '/').lower(),
                self.__class__.__name__.lower()
            )
            if not exists(join(TEMPLATE_PATH, filename)):
                filename = '%s/%s.html' % (
                    self.__module__[5:].replace('.', '/').lower(),
                    re.sub('([A-Z])', r'-\1',self.__class__.__name__)[1:].lower()
                )
        self.finish(render._render(filename, **kwargs))

    login = login
    logout = logout

    # def on_finish(self):
    #     pass
    #     #self.db.close()

class LoginView(View):
    def prepare(self):
        super(LoginView, self).prepare()
        if not self.current_user_id:
            return self.redirect('/login')

# class JsonView(View):
#     def finish(self, arg=None):
#         self.set_header('Content-Type', 'application/json; charset=UTF-8')
#         if arg and not isinstance(arg, basestring):
#             arg = json.dumps(arg)
#         super(JsonView, self).finish(arg)

# class JsonLoginView(JsonView):
#     def prepare(self):
#         super(JsonLoginView, self).prepare()
#         if self._finished:
#             return
#         if not self.current_user_id:
#             self.finish({'err':ERR.NO_LOGIN})

# class JsonUserView(JsonLoginView):
#     def prepare(self):
#         super(JsonUserView, self).prepare()
#         if self._finished:
#             return
#         if self.user.level == USER_LEVEL.BAN:
#             self.finish({'err':ERR.PERMISSION_DENIED})

class NoLoginView(View):
    def prepare(self):
        if self.current_user_id:
            self.redirect('/')

class AdminView(LoginView):
    def prepare(self):
        super(AdminView, self).prepare()
        if not self.current_user.is_admin:
            return self.redirect('/')

# class JsonAdminView(JsonLoginView):
#     def prepare(self):
#         super(JsonAdminView, self).prepare()
#         u = self.current_user
#         if u and u.level != USER_LEVEL.ADMIN:
#             self.finish({'err':ERR.PERMISSION_DENIED})
#             return

if __name__ == '__main__':
    s = Session()
    from model.models import Post
    query = s.query(Post)
    for i in query:
        print i.title
