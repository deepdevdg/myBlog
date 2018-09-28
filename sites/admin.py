# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sites.custom_model_admin import ReadOnlyModelAdmin
from django.contrib import  admin
from .models import Article#,Publisher,Author,Book
from sites import models
from django.contrib.admin.models import LogEntry
#清除最近的歷史紀錄
LogEntry.objects.all().delete()
# admin.site.register(models.UserInfo)
admin.site.register(models.Dept)
class UserInfoAdmin(admin.ModelAdmin):
#class UserInfoAdmin(ReadOnlyModelAdmin):
    list_display = ('name', 'age', 'gender', 'dept')
    # 设置哪些字段可以点击进入编辑界面，与list_editable 冲突
    #list_display_links = ('name', 'age')
    #开启搜索功能，按名字和年龄
    search_fields = ('name', 'age')
    #开启过滤器
    list_filter = ('gender', 'dept')
    #开启分页
    list_per_page = 3
    #外键搜索框，选项多时用
    raw_id_fields = ('dept',)
    #filter_horizontal = ()
    #在显示列表中直接修改
    list_editable = ('age', 'gender', 'dept')
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-age',)
    #自定义操作列表
    actions = ('test_action','set_age_zero')
    def test_action(self):
        pass
    def set_age_zero(self, request, queryset):
        for UserInfo in queryset:
            UserInfo.age = 0
            UserInfo.save()
    set_age_zero.short_description = u'年龄清零'
admin.site.register(models.UserInfo, UserInfoAdmin)

class ArticleAdmin(admin.ModelAdmin):
#class ArticleAdmin(ReadOnlyModelAdmin):
     list_display = ('title', 'update_time')

#admin.site.register(Article)
admin.site.register(Article,ArticleAdmin)
#admin.site.register(Publisher)#注册Publisher
#admin.site.register(Author)#注册Author
#admin.site.register(Book) #注册Book
# Register your models here.
