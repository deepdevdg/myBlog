# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Article(models.Model):
    title = models.CharField('标题', max_length=200)
    url = models.CharField('地址', max_length=200)
    body = models.TextField('内容')
    create_date = models.DateTimeField('创建时间', )
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    #让Django在打印对象时显示一些我们指定的信息。
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

class UserInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name="员工姓名",default="例：张三2")
    age = models.PositiveSmallIntegerField("年龄",default="35")
    gender_choice = ((1, "男性"), (2, "女性"))
    gender = models.SmallIntegerField("性别", choices=gender_choice,default="1")
    dept = models.ForeignKey('Dept', models.CASCADE, verbose_name="部门")
    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = "员工信息表"
    def __str__(self):
        return self.name

class Dept(models.Model):
    name = models.CharField(max_length=32, verbose_name="部门名称")
    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门表"
    def __str__(self):
        return self.name

class UserPwdTest(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    class Meta:
        verbose_name = "密码保存测试表"
        verbose_name_plural = "密码保存测试表"
    def __str__(self):
        return self.user
# Create your models here.
