#!/usr/bin/env python
# coding=utf-8

from base import BaseHandler
import tornado.web
import tornado.gen

import time

# 同步
'''
class SleepHandler(BaseHandler):
    def get(self):
        time.sleep(17)
        self.render("sleep.html")
'''

# 异步 1
'''
class SleepHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 17, callback=self.on_response)
    def on_response(self):
        self.render("sleep.html")
        self.finish()
'''

# 异步 2
class SleepHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 17)
        #yield tornado.gen.sleep(17)
        self.render("sleep.html")

class SeeHandler(BaseHandler):
    def get(self):
        self.render("see.html")