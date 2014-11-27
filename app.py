#!/usr/bin/python3
# coding: utf-8
import lib.patch
import tornado
import tornado.ioloop
import config
import view._site
from view._route import route
from tornado.web import StaticFileHandler

print tornado.version
#from view.postcard import route as route_postcard

application = tornado.web.Application(
    route.handlers,
    debug=config.DEBUG
)

#application.add_handlers(*route_postcard.subdomain_handlers)

if __name__ == "__main__":
    import sys
    print(sys.version)
    print("listen: %s" % config.PORT)
    tornado.log.enable_pretty_logging()
    application.listen(config.PORT)
    tornado.ioloop.IOLoop.instance().start()
