# -*- coding: utf-8 -*-
import scrapy
from dytt.items import DyttItem
from urllib.parse import urljoin
import re
class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ['dy2018.com']


    def start_requests(self):
        for i in range(2,self.settings.get("PAGE")):
            url = "https://www.dy2018.com/html/gndy/dyzz/index_{}.html".format(i)
            yield scrapy.Request(url,callback = self.parse)

    def parse(self, response):
        table_list = response.xpath("//div[@class='co_content8']/ul//table")

        for table in table_list:
            href = table.xpath(".//tr[2]//td[2]/b/a/@href").extract_first()
            href = urljoin(response.url,href)
            yield scrapy.Request(href,callback = self.parse_details)


    def parse_details(self,response):
        item  = DyttItem()
        text =response.text
        try:
            item['film_name'] = re.findall("◎片　　名　(.*?)</p>",text)[0]
            item["url"] = response.url
            item["origin"] = re.findall("◎产　　地　(.*?)</p>",text)[0]
            item["classify"] = re.findall("◎类　　别　(.*?)</p>",text)[0]
            item["language"] = re.findall("◎语　　言　(.*?)</p>",text)[0]
            item["publish_time"] = re.findall("◎上映日期　(.*?)</p>",text)[0]
            item["film_time"] = re.findall("◎片　　长　(.*?)</p>",text)[0]
            item["db_judge"] = re.findall("◎豆瓣评分　(.*?)</p>",text)[0]
            item["actors"] = re.findall("◎主　　演　(.*?)</p>",text,re.S)[0].replace("&middot;","·")
            item["director"] = re.findall("◎导　　演　(.*?)</p>",text)[0].replace("&middot;",'·')
            item["img"] = response.xpath("//div[@id = 'Zoom']/p[1]/img/@src").extract_first()
        except:
            item["origin"] = "\\"


        yield item
