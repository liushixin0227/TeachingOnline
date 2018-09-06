#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 下午11:38
# @Author  : Liushixin
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from organization.models import CityDict, CourseOrg, Teacher


@xadmin.sites.register(CityDict)
class CityDictAdmin(object):
    list_display = ['name', 'describe', 'create_time']
    search_fields = ['name', 'describe']
    list_filter = ['name', 'create_time', 'describe']


@xadmin.sites.register(CourseOrg)
class CourseOrgAdmin(object):
    list_display = ['name', 'describe', 'click_nums', 'fav_nums',
                    'image', 'address', 'city', 'create_time']
    search_fields = ['name', 'describe', 'click_nums', 'fav_nums',
                     'image', 'address', 'city']
    list_filter = ['name', 'describe', 'click_nums', 'fav_nums',
                   'image', 'address', 'city', 'create_time']


@xadmin.sites.register(Teacher)
class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company',
                    'work_position', 'characteristic', 'click_nums', 'fav_nums', 'create_time']
    search_fields = ['org', 'name', 'work_years', 'work_company',
                     'work_position', 'characteristic', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company',
                   'work_position', 'characteristic', 'click_nums', 'fav_nums', 'create_time']
