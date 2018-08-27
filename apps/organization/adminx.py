#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 下午11:38
# @Author  : Liushixin
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from organization.models import CityDict


class CityDictAdmin(object):
    list_display = ['name', 'create_time']
    search_fields = ['name']
    list_filter = ['name', 'create_time']


xadmin.site.register(CityDict, CityDictAdmin)
