# -*- coding: utf-8 -*-

# Scrapy settings for demo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

#import sys
#import os
#from os.path import dirname
#path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
#sys.path.append(path)
#from misc.log import *

BOT_NAME = 'demo'

SPIDER_MODULES = ['demo.spiders']
NEWSPIDER_MODULE = 'demo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demo (+http://www.yourdomain.com)'

#DOWNLOADER_MIDDLEWARES = {
#    # 'misc.middleware.CustomHttpProxyMiddleware': 400,
#    'misc.middleware.CustomUserAgentMiddleware': 401,
#}

ITEM_PIPELINES = {
    'demo.pipelines.ImageDPipeline': 303,
#    'demo.pipelines.JsonWithEncodingPipeline': 300,
#    'demo.pipelines.RedisPipeline': 301,
}

IMAGES_STORE = '/Users/Sunxiaolu/Google\ Drive/recommend/crawler/demo'

IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}

IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110

LOG_LEVEL = 'INFO'

DEPTH_LIMIT = 10

DOWNLOAD_DELAY = 1
