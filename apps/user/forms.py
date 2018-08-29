#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 0029 15:33
# @Author  : Liushixin
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from captcha.fields import CaptchaField
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})
