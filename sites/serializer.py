# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import UserInfo,Dept,Article
#model指定对应的模型实体，fields指定要序列化的数据域（可理解为数据库表的某一列）。
class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        #fields = ('name', 'age','gender','dept')
        fields = '__all__'  # all model fields will be included
class DeptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dept
        #fields = ('name',)
        fields = '__all__'  # all model fields will be included
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'url','body','create_date','update_time')
