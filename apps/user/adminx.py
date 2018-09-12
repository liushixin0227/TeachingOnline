#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 0024 18:07
# @Author  : Liushixin
# @Site    :
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from user.models import EmailVerifyRecord, Banner
from xadmin import views


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '在线教育后台管理'
    site_footer = 'Liushixin 2018'
    menu_style = 'accordion'


@xadmin.sites.register(EmailVerifyRecord)
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


@xadmin.sites.register(Banner)
class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'create_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'create_time']
