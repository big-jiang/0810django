#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'Jack'

import os
import sys
import random
import django
from datetime import date

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_xadmin.settings'  # 设置项目的配置文件
django.setup()

from blogxadmin.models import Article # 将模型导入放在django注册启动之后


def import_data():
    Article.objects.bulk_create([Article(title=f"第{i}篇文章的标题",
                                         brief_content=f"第{i}篇文章的摘要",
                                         content=f"第{i}篇文章的主要内容：这是一个测试Xadmin的Djang项目",
                                         publish_date=date(random.randint(2017, 2019), random.randint(1, 12), random.randint(1, 28)))
                                for i in range(1, 15)])
    return True


if __name__ == "__main__":
    if import_data():
        print("数据导入成功！")

