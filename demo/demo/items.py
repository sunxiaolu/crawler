# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pubdate = scrapy.Field()
    type = scrapy.Field()
    site_name = scrapy.Field()
    id = scrapy.Field()
    author=scrapy.Field()
    keywords = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    pass
