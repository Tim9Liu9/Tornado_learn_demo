#!/usr/bin/env python
#coding:utf-8


import tornado.web
import methods.readdb as mrd
from base import BaseHandler


# class IndexHandler(tornado.web.RequestHandler):
class IndexHandler(BaseHandler):    #继承base.py中的类BaseHandler
    def get(self):
        # greeting = self.get_argument('greeting', 'Hello')
        # self.write(greeting + ', welcome you to read: www.itdiffer.com')
        # self.render("index.html")
        usernames = mrd.select_columns(table="users",column="username")
        one_user = usernames[0][0]
        self.render("index.html", user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                # self.write("welcome you: " + username)
                # self.set_cookie(username,db_pwd) #设置cookie self.write(username)
                # self.set_secure_cookie(username,db_pwd)
                self.set_current_user(username)    #将当前用户名写入cookie，方法见下面
                self.write(username)
            else:
                # self.write("your password was not right.")
                self.write("-1")
        else:
            # self.write("There is no this user.")
            self.write("-1")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))    #注意这里使用了tornado.escape.json_encode()方法
        else:
            self.clear_cookie("user")

class ErrorHandler(BaseHandler):    #增加了一个专门用来显示错误的页面
    def get(self):                                        #但是后面不单独讲述，读者可以从源码中理解
        self.render("error.html")