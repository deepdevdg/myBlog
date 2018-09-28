# -*- coding: utf-8 -*-
from rest_framework import routers
from .views import UserInfoViewSet,DeptViewSet,ArticleViewSet
router = routers.DefaultRouter()
router.register(r'userinfo', UserInfoViewSet)
router.register(r'dept', DeptViewSet)
router.register(r'article', ArticleViewSet)