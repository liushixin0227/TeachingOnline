#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 0007 11:52
# @Author  : Liushixin
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from organization.views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescribeView

urlpatterns = [
    url('^list/$', OrgView.as_view(), name='orglist'),
    url('^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url('^home/(?P<org_id>\d+)', OrgHomeView.as_view(), name='org_home'),
    url('^course/(?P<org_id>\d+)', OrgCourseView.as_view(), name='org_course'),
    url('^describe/(?P<org_id>\d+)', OrgDescribeView.as_view(), name='org_describe'),
    url('^teacher/(?P<org_id>\d+)', OrgTeacherView.as_view(), name='org_teacher'),
]
