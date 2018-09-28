# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.login, name='index'),
    #url(r'^$', views.register, name='index'),
    url(r'^$', views.login),
    #二级目录访问地址是/polls/register
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    #url(r'^$', views.login, name='index'),
    #url(r'^register/',views.register),
    #url(r'^register/', views.register, name='register'),
    #url(r'^logout/', views.logout, name='logout'),
]