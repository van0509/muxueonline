#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Seven°
@contact: free001@vip.qq.com
@software: PyCharm
@file: adminx.py
@time: 2018-09-06 14:49
"""

from .models import UserAsk, CourseCommnets, UserFavorite, UserMessage, UserCourse
import xadmin


class UserAskAdmin(object):
    list_display = ['name', 'moblie', 'course_name', 'add_time']
    search_fields = ['name', 'moblie', 'course_name']
    list_filter = ['name', 'moblie', 'course_name', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)


class CourseCommnetsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


xadmin.site.register(CourseCommnets, CourseCommnetsAdmin)


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


xadmin.site.register(UserFavorite, UserFavoriteAdmin)


class UserMessageAdmin(object):
    list_display = ['name', 'message', 'has_read', 'add_time']
    search_fields = ['name', 'message', 'has_read']
    list_filter = ['name', 'message', 'has_read', 'add_time']


xadmin.site.register(UserMessage, UserMessageAdmin)

class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserCourse, UserCourseAdmin)
