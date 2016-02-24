#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""

import sys     #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.sleep import SleepHandler, SeeHandler

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler),
    (r'/sleep', SleepHandler),
    (r'/see', SeeHandler),
]