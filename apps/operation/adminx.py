#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 0027 13:34
# @Author  : Liushixin
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from operation.models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


@xadmin.sites.register(UserAsk)
class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'create_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'create_time']


@xadmin.sites.register(CourseComments)
class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'create_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'create_time']


@xadmin.sites.register(UserFavorite)
class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'create_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'create_time']


@xadmin.sites.register(UserMessage)
class UserMessageAdmin(object):
    list_display = ['user', 'message', 'is_read_status', 'create_time']
    search_fields = ['user', 'message', 'is_read_status']
    list_filter = ['user', 'message', 'is_read_status', 'create_time']


@xadmin.sites.register(UserCourse)
class UserCourseAdmin(object):
    list_display = ['user', 'course', 'create_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'create_time']
