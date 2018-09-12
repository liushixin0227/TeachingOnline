#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 0027 14:30
# @Author  : Liushixin
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from courses.models import Course, Lesson, Video, CourseResource


@xadmin.sites.register(Course)
class CourseAdmin(object):
    list_display = ['name', 'describe', 'detail', 'degree', 'learn_times',
                    'students', 'fav_num', 'image', 'click_num', 'create_time']
    search_fields = ['name', 'describe', 'detail', 'degree',
                     'students', 'fav_num', 'image', 'click_num']
    list_filter = ['name', 'describe', 'detail', 'degree', 'learn_times',
                   'students', 'fav_num', 'image', 'click_num', 'create_time']


@xadmin.sites.register(Lesson)
class LessonAdmin(object):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'create_time']


@xadmin.sites.register(Video)
class VideoAdmin(object):
    list_display = ['lesson', 'name', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'create_time']


@xadmin.sites.register(CourseResource)
class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'create_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'create_time']
