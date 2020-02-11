# -*- coding: utf-8 -*-

from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)


# worker
class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    # 姓名
    name = models.CharField(max_length=20)
    # 身份证号
    id_number = models.CharField(max_length=20)
    # 进入公司的时间
    register_date = models.DateField()
    # 最近工作的时间
    last_work_date = models.DateField()
    # 是否在职
    is_office = models.BooleanField(default=True)


# product
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    # 产品名称
    name = models.CharField(max_length=20)
    # 状态 有 在销售，缺货，停售
    status = models.CharField(max_length=10)
    # 仓库中拥有的数量
    owned_number = models.IntegerField()
    # 最近一次进货时间
    last_supple_date = models.DateTimeField()
    # 多对多worker
    worker = models.ManyToManyField("Worker", through="Delivery")


class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    worker_id = models.ForeignKey('Worker', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    # 历史发送量
    total_number = models.IntegerField()
    last_delivery_date = models.DateTimeField(auto_now=True)
    today_number = models.IntegerField()
    today_data = models.DateTimeField()


# 交易订单
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)

    worker_id = models.ForeignKey('Worker', on_delete=models.CASCADE)

    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)

    product_number = models.IntegerField()

    create_date = models.DateTimeField(auto_now_add=True)
