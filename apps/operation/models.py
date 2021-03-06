from datetime import datetime

from django.db import models

# Create your models here.
from courses.models import Course
from user.models import UserProfile


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50, verbose_name='课程名')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    comments = models.CharField(max_length=200, verbose_name='评论')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    fav_id = models.IntegerField(default=0, verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '课程机构'), (3, '讲师')), default=1, verbose_name='收藏类型')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='接受用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    is_read_status = models.BooleanField(default=False, verbose_name='读取状态')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '消息通知'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
