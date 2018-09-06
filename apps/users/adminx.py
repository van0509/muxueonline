#!/usr/bin/python3
# coding:utf-8
import xadmin
from xadmin import views
from .models import *

"""
@author: Seven°
@contact: free001@vip.qq.com
@software: PyCharm
@file: adminx.py
@time: 2018-08-30 0:20
"""
class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSetting(object):
    site_title=u'幕学后台管理系统'
    site_footer=u'幕学在线网'
    menu_style='accordion'

xadmin.site.register(views.CommAdminView,GlobalSetting)

xadmin.site.register(views.BaseAdminView,BaseSetting)

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']

xadmin.site.register(Banner,BannerAdmin)
