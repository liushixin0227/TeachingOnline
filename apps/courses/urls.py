#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 0013 10:16
# @Author  : Liushixin
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from courses.views import CoursesListView

urlpatterns = [
    url('^list/$', CoursesListView.as_view(), name='course_list'),

]
