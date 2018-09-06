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
    password = forms.CharField(required=True, min_length=5,
                               widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5,
                               widget=forms.PasswordInput)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True, label='password',
                               widget=forms.PasswordInput)
    password_confirmed = forms.CharField(required=True, label='password_confirmed',
                                         widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(ModifyPwdForm, self).clean()
        password = cleaned_data.get('password')
        password_confirmed = cleaned_data.get('password_confirmed')
        if password != password_confirmed:
            raise forms.ValidationError('两次密码必须一致')
