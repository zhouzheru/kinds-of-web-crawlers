# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanItem(scrapy.Item):
    city = scrapy.Field()
    id= scrapy.Field()
    name = scrapy.Field()
    dp_url = scrapy.Field()
    address = scrapy.Field()
    score = scrapy.Field()
    telephone = scrapy.Field()
    opentime = scrapy.Field()
