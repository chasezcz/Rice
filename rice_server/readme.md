# 修改数据库

## 修改文件

rice_server/rice_model/models.py 中定义table的属性

## 调用django支持创建数据表

创建表结构

`$ python manage.py migrate`

让 Django 知道我们在我们的模型有一些变更

`$ python manage.py makemigrations rice_model`

创建表结构

`$ python manage.py migrate rice_model`
