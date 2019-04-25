# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyttItem(scrapy.Item):
    film_name = scrapy.Field()
    url = scrapy.Field()
    origin = scrapy.Field()
    classify =scrapy.Field()
    publish_time = scrapy.Field()
    actors = scrapy.Field()
    director = scrapy.Field()
    film_time =scrapy.Field()
    language =scrapy.Field()
    db_judge=scrapy.Field()
    img = scrapy.Field()
