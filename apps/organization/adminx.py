#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Seven°
@contact: free001@vip.qq.com
@software: PyCharm
@file: adminx.py
@time: 2018-09-06 15:07
"""
from .models import CityDict, CourseOrg, Teacher
import xadmin


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', ]
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'add_time']


xadmin.site.register(Teacher, TeacherAdmin)
