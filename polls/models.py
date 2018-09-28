# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
#
class Userlg(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=128,unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    ac_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ["-ac_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
# # Create your models here.
