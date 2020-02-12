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
from rice_server.views import *

urlpatterns = [
    # 用户相关
    path('prod-api/user/login', user.login),
    path('prod-api/user/info', user.info),
    # 仓库相关
    path('prod-api/warehouse/getDeliveryInfo', warehouse.get_delivery_info),
    path('prod-api/warehouse/delivery', warehouse.delivery),
    path('prod-api/warehouse/collect', warehouse.collect),
    # 产品相关
    path('prod-api/product/all', product.all),
    path('prod-api/product/add', product.add),
    # 职工相关
    path('prod-api/worker/all', worker.all),
    path('prod-api/worker/add', worker.add)
]
