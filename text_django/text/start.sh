#! /bin/bash
# 启动ssh 脚本即可
ps -ef | grep python3|awk '{print $2}'|xargs kill -9  # 杀死所有python3启动的进程
python3 manage.py migrate   # 创建表结构
python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate TestModel   # 创建表结构
python3 manage.py runserver 0.0.0.0:8002
