# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from  models import  Article,UserInfo,Dept
# from django import forms
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from sites import models
import django_filters
from rest_framework import viewsets,filters
from .serializer import UserInfoSerializer,DeptSerializer,ArticleSerializer
#from django.contrib.auth.decorators import login_required
# Create your views here.
class UserInfoViewSet(viewsets.ModelViewSet):
    #swager加restful操作注释不要取消注释符
    """
        retrieve:
            Return a user instance.
        list:
            Return all users, ordered by most recently joined.
        create:
            Create a new user.
        delete:
            Remove an existing user.
        partial_update:
            Update one or more fields on an existing user.
        update:
            Update a user.
        """
    #结果集默认按照名字字段倒序显示
    queryset = UserInfo.objects.all().order_by('-name')
    serializer_class = UserInfoSerializer
    # 配置搜索功能和排序功能
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,)
    # 设置在界面搜索的关键字
    search_fields = ('name',)
    # 设置需要在界面被排序的字段
    ordering_fields = ('age',)
class DeptViewSet(viewsets.ModelViewSet):
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer
    filter_backends = (filters.SearchFilter,)
    # 设置搜索的关键字=name 表示完全匹配
    search_fields = ('=name',)
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    # 设置搜索的关键字
    search_fields = ('title',)

#@login_required
def index(request):
    # return HttpResponse('Hello!')
    #return  render(request,'index.html')
    # data = [1, 2, 3, 4, 5, 6]
    #序列化列表[]前端頁面要加safe,如果{}json不要
    data = ['hello', 'worldj', '!']
    data = json.dumps(data)  # data必须是一个list
    words = 'Worldw!'
    #return render(request, 'index.html', context={'words': words})
    #return render(request, 'index.html', locals())
    context = {}
    #context['hello'] = 'Hello World!'
    # return render(request,'index.html',context)
    #return redirect("https://www.163.com")
    list = ['view', 'Json', 'JS']
    list = json.dumps(list)
    # return render(request, 'index.html', {'List': json.dumps(list),})
    articles =  Article.objects.all()
    #return render(request, 'index.html', {'articles': articles})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #在终端可以打印观察用户名和密码
        print(username, password)
        # 将数据保存到数据库
        models.UserPwdTest.objects.create(user=username, pwd=password)
        user_list = []
        # temp = {'user': username, 'pwd': password}
        # user_list.append(temp)
        # 从数据库中读取所有数据相当于SQL中的SELECT * FROM
        user_list = models.UserPwdTest.objects.all()
    return render(request, 'index.html', locals())

def article_list(request):
    articles = Article.objects.all()
    #将article表中的所有对象赋值给articles这个变量，它是一个列表
    return render(request, 'index.html', {'articles': articles})
    #生成一个article变量，这个变量可以给templates中的html文件使用

def scene(request):
    if request.method == "GET":
            name = request.GET.get('domain_name')
            print (name)
            result = "OK!"
            return HttpResponse(result)

# class ArticleForm (forms.ModelForm):
#     class Meta:
#         model=Article
#         fields =('title','url','body','create_date','update_time')
#解决CSRF告警问题
@csrf_exempt
def ajax(request):
    if request.method=='POST':
        print(request.POST)
        data={'status':0,'msg':'请求成功','data':[11,22,33,44]}
        #return HttpResponse(json.dumps(data))
        return JsonResponse(data)  # 后来写法
    else:
        return render(request,'ajax.html')

#接口调用测试
def api_test(request):
    if request.method == "POST":
        data = json.loads(request.POST.get('data'))
        serializer_obj = DeptSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
    return render(request,'api_test.html',locals())
#文本框按json格式输出{ "name": "gmtest1" }便可插入一条记录