# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义项目所需爬取的字段
class ComplaintspiderItem(scrapy.Item):
    # 投诉帖子编号
    number = scrapy.Field()
    # 投诉帖子题目
    title = scrapy.Field()
    # 投诉帖子内容
    content = scrapy.Field()
    # 投诉帖子链接
    url = scrapy.Field()
