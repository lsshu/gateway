# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from django.contrib.auth.models import User
from blogs.models import BlogCategory

class MyscrapyPipeline:
    def process_item(self, item, spider):
        category = BlogCategory.objects.get(id=1)
        user = User.objects.get(id=1)
        print('打开数据库')
        item['category'] = category
        item['user'] = user
        item.save()  # 数据将会自动添加到指定的表
        print('关闭数据库')
        return item
