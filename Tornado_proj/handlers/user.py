#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
import tornado.escape
from base import BaseHandler

# class UserHandler(tornado.web.RequestHandler):
class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        #username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        self.render("user.html", users = user_infos)

