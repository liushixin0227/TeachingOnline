#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 0007 14:25
# @Author  : Liushixin
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
import re

from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name', ]

    def clean(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法')
