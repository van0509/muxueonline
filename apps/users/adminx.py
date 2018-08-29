#!/usr/bin/python3
#coding:utf-8
import xadmin
from .models import *
"""
@author: Seven°
@contact: free001@vip.qq.com
@software: PyCharm
@file: adminx.py
@time: 2018-08-30 0:20
"""
class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)