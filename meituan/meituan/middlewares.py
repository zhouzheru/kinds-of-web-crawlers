# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random


class ProxyMiddleware(object):

    def process_item(self,requests,spider):

        request.meta["proxy"] = random.choice(spider.settings.get("PROXIES_LIST"))
