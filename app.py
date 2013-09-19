#!/usr/bin/python
# coding: utf-8
import _envi
from sys import argv
import tornado.ioloop
import config
import view._site
from os.path import join
from view._route import route
#from view.postcard import route as route_postcard


application = tornado.web.Application(
    route.handlers,
    debug=config.DEBUG,
    static_path=join(_envi.PREFIX, 'static'),
    cookie_secret="6aOO5ZC55LiN5pWj6ZW/5oGo77yM6Iqx5p+T5LiN6YCP5Lmh5oSB44CC",
)

#application.add_handlers(*route_postcard.subdomain_handlers)

if __name__ == "__main__":
    application.listen(config.PORT)
    tornado.ioloop.IOLoop.instance().start()        
