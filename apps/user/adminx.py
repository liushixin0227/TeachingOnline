#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 0024 18:07
# @Author  : Liushixin
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from user.models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'create_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'create_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
