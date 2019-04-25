# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo

import os
import time
import requests


class MongoPipeline():
    def __init__(self,mongo_url,mongo_db):
        self.mongo_db = mongo_db
        self.mongo_url  =mongo_url

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
        mongo_db = crawler.settings.get("MONGO_DB"),
        mongo_url = crawler.settings.get("MONGO_URL")
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        self.db["movieinfo"].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()


class DownloadPipline(): #用于下载电影海报

    def process_item(self,item,spider):

        if not os.path.exists("imglist"):
            os.mkdir("./imglist")
        if item.get("film_name") and item.get("img"):
            filename = item.get("film_name")+".jpg"
            post_url = item["img"]
            filepath = "F:\\data\\Python\\Scrapy\\dytt\\dytt\\imglist"
            filepath = filepath+'\\'+filename
            with open(filepath,"wb")as f:
                f.write(requests.get(item["img"]).content)
        return item
        # print(item["img"])
