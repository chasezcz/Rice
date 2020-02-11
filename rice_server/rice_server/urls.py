# -*- coding: utf-8 -*-
"""rice_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # 用户相关
    path('prod-api/user/login', views.user_login),
    path('prod-api/user/info', views.user_info),
    # 仓库相关
    path('prod-api/warehouse/getDeliveryInfo/', views.get_delivery_info),
    path('prod-api/warehouse/delivery/', views.delivery),
    path('prod-api/warehouse/collect/', views.collect)
]
