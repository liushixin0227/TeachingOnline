#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 0030 23:50
# @Author  : Liushixin
# @Site    : 
# @File    : email_send.py
# @Software: PyCharm
import random
import string
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TeachingOnline.settings")  # project_name 项目名称
django.setup()
from django.core.mail import send_mail

from TeachingOnline.settings import EMAIL_FROM
from user.models import EmailVerifyRecord


def make_random_str(randomlength=8):
    random_str = ''.join(random.sample(
        string.ascii_letters + string.digits, randomlength))
    return random_str


def send_register_email(email, send_type='register'):
    code = make_random_str(16)
    email_record = EmailVerifyRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = '在线教育网站注册激活链接'
        email_body = '请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        print(send_status)
