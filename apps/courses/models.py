from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models

# Create your models here.
from organization.models import CourseOrg


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name='课程机构', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='课程名')
    describe = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(max_length=20, choices=(
        ('Junior', '初级'), ('Medium', '中级'), ('Advanced', '高级')), verbose_name='课程难度')
    category = models.CharField(max_length=20, verbose_name='课程类别', default='')
    tag = models.CharField(max_length=100, verbose_name='课程标签', default='')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟)')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(max_length=100, upload_to=r'image/%Y/%m/%d', verbose_name='封面图片')
    click_num = models.IntegerField(default=0, verbose_name='课程点击数')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def users(self):
        return self.usercourse_set.all()[:5]

    def lesson_num(self):
        return self.lesson_set.all().count()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='视频资源')
    download = models.FileField(upload_to=r'video_resource/%Y/%m/%d', verbose_name='资源文件')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '视频资源'
        verbose_name_plural = verbose_name
