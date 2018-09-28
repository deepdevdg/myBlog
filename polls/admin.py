# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question,Userlg

class QuestionAdmin(admin.ModelAdmin):
    #显示的字段
    list_display = ('pub_date', 'question_text')
    #只能修改的字段
    fields = ('pub_date',)
    view_on_site = False
admin.site.register(Question, QuestionAdmin)

class UserlgAdmin(admin.ModelAdmin):
    #显示的字段
    list_display = ('name', 'password','sex','email','ac_time')
admin.site.register(Userlg,UserlgAdmin)
# Register your models here.
