#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 0007 11:52
# @Author  : Liushixin
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from organization.views import OrgView, AddUserAskView

urlpatterns = [
    url('^list/$', OrgView.as_view(), name='orglist'),
    url('^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
]
