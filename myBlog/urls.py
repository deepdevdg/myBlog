# -*- coding: utf-8 -*-
"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
#from django.views.generic import TemplateView
from sites import  views
from sites.urls import router as sites_router
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="API docs 发布站点")
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from polls import views as view2
# from sites.views import *
urlpatterns = [
    url(r'^$',views.index),
    url(r'^sites/article/',views.article_list),
    url(r'^article/', views.article_list),
    url(r'^ajax/', views.ajax),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^api/', include(sites_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r"^docs/$", schema_view),
    #url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^api-test/',views.api_test,name='api_test'),
    url(r'^api-auth/', obtain_jwt_token),
    url(r'^polls/', include('polls.urls')),
    url(r'^login/', view2.login),
    url(r'^logout/', view2.logout),
    url(r'^register/', view2.register),
    url(r'^captcha', include('captcha.urls')),

 #   url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]
