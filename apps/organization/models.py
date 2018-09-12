from datetime import datetime

from django.db import models


# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市')
    describe = models.TextField(verbose_name='城市描述')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    describe = models.TextField(verbose_name='机构描述')
    category = models.CharField(verbose_name='机构类别', max_length=30,
                                choices=(('education_institution', '教育机构'),
                                         ('personal', '个人'),
                                         ('company', '企业')), default='education_institution')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(max_length=100, upload_to='org/%Y/%m/%d', verbose_name='封面图')
    address = models.CharField(max_length=150, verbose_name='机构地址')
    student_num = models.IntegerField(default=0, verbose_name='学习人数')
    course_nums = models.IntegerField(default=0, verbose_name='课程数')
    city = models.ForeignKey(CityDict, verbose_name='所在城市')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='讲师姓名')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    characteristic = models.CharField(max_length=50, verbose_name='教学特点')
    image = models.ImageField(max_length=100, upload_to='teacher/%Y/%m/%d', verbose_name='讲师头像', default='')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '讲师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
