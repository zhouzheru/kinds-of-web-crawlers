# -*- coding: utf-8 -*-
import scrapy
from meituan.items import MeituanItem
from urllib.parse import urljoin
from urllib.parse import urlencode
import json
import random
import time


class MtSpider(scrapy.Spider):
    name = 'MT'
    allowed_domains = ['meituan.com']
    url = 'https://www.meituan.com/changecity/'
 #登录后复制的cookies
    cookies="_lxsdk_cuid=16a54648b98c8-0cac66a7859ac8-3d644601-100200-16a54648b98c8; _hc.v=199e0477-cc49-ff4e-47ed-8336a270f2e6.1556199434; mtcdn=K; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=16a54648b98c8-0cac66a7859ac8-3d644601-100200-16a54648b98c8; lat=32.68817; lng=109.041088; lt=flbcxKN4DBOiikB9WqHX52naO3oAAAAAUggAACsEhNMfqvZo828J6u_2hYsIn5dejWRTaHmuVxpJXCv7KmoL0EultCDkcj0q1HK_Mg; u=125800272; n=IUQ577626871; token2=flbcxKN4DBOiikB9WqHX52naO3oAAAAAUggAACsEhNMfqvZo828J6u_2hYsIn5dejWRTaHmuVxpJXCv7KmoL0EultCDkcj0q1HK_Mg; unc=IUQ577626871; uuid=2fe2b9eb52d44c71b1cc.1556675120.3.0.0; ci=10; rvct=10%2C359%2C1%2C588%2C56%2C59%2C92%2C1102%2C116%2C324%2C1074; __mta=176076317.1556194054498.1556542323637.1556675090243.7; client-id=dd2a374f-b5c7-471e-a1ff-89c59fbc0032; _lxsdk_s=16a710ff0f7-450-2af-dac%7C%7C18"

    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
    page = 1

    def before_request(self):

        params={
        'cateId': '0',
         'areaId': '0',
          'sort': '',
          'dinnerCountAttrId': '',
          'page': self.page,
          'userId': '',
           'uuid': '807cb442065d4e208a33.1556244342.1.0.0',
           'platform': '1',
            'partner': '126',
            'originUrl': 'https%3A%2F%2Fbj.meituan.com%2Fmeishi%2Fpn1%2F',
             'riskLevel': '1',
              'optimusCode': '1',

               '_token':"eJx9j1GPojAUhf9LX5dIgSkVk31wEASVoQISdDMP0KnAiIgUQZnsf99OdjbZfdnkJuf0uycntx+gdd/ATIHQgFACPWvBDCgTONGBBDouNgjpOkZPEGOkSID+y6YISyBr4wWY/VA0XZcUBF8/SSDAb4L16av0l1WfxHxmXBEBRdc1fCbLvJicWdnd0npCL2dZeF6UclOrsrjj/yEgys6RKBN6+tL0S7s/b098SzTxMq+FY6uheo86fz5au+DIwuG6k9+1fHmyH3ls5Rdn2w+qOT2sv/kEL+mpaxaGaxfbyonzwIkJTRJ/rFLYGshF5ViQIdLJy9VF/WHsE8Pw7kY41K1L3qzNLoDHKr/Z6gsv2BiuUdD6bqYlY3q3mghuYLxnXmxqZcbpnZnqc2WFpp3x5Vb1rlHIA+5Yj3PWVEtOr0Wboi2U6XNPaZksGPflZr4x1mbiDc6FaHy+2ie1GezJERsqt287GisNgfoQhwTPVweGk7EOwsfwHfz8BViZm9A="
               } #_token 相当于cookies，动态变化，不过可以发现不修改也可以访问
        return params


    def start_requests(self):
        yield scrapy.Request(self.url,callback=self.parse,cookies=self.cookies,dont_filter=True)


    def parse(self, response):

        div_list = response.xpath("//div[@class='alphabet-city-area']//div")

        for div in div_list:
            citys = div.xpath("./span[2]//a")
            for city in citys:
                item = MeituanItem()
                item["city"] = city.xpath("./text()").extract_first()

                city_url= city.xpath("./@href").extract_first()

                city_url= urljoin(response.url,city_url)

                yield scrapy.Request(url = city_url+"/meishi/",callback = self.parse_url,meta={"item":item})


    def parse_url(self,response):


        item = response.meta["item"]
        city = item["city"]

        base_url = response.url+"api/poi/getPoiList?cityName="+city+"&"
        self.page =1 #这里先传入page=1，访问url，可以得出具体条目，然后在访问剩余的page=2-N

        url = base_url+urlencode(self.before_request())

        yield scrapy.Request(url,callback=self.parse_details,meta={"base_url":base_url,"item":item})


    def parse_details(self,response):
        item  = response.meta["item"]
        base_url =response.meta["base_url"]
        text = response.text

        text = json.loads(text)


        totalCounts =text.get("data").get("totalCounts")
        poiInfos = text.get("data").get("poiInfos")

        for each in poiInfos:
            item["id"] = each.get("poiId")
            item["dp_url"]= 'https://www.meituan.com/meishi'+"/"+str(item["id"])+"/"
            yield scrapy.Request(url=item["dp_url"],callback = self.parse_dp_details,meta={"item":item})

        #确定页数
        pages  = totalCounts // 15 +1
        for page in range(2,pages+1):
            self.page = page
            url=base_url+urlencode(self.before_request())

            yield scrapy.Request(url=url,callback = self.parse_details,cookies=self.cookies,meta={"base_url":base_url,"item":item})

    def parse_dp_details(self,response):
        item  = response.meta["item"]

        # print(response.url)
        text = response.xpath("//body//script[last()-2]//text()").extract_first().rstrip(";").lstrip("window._appState = ")

        if text:
            text = json.loads(text)
            item["name"] = text.get('detailInfo').get("name")
            item["address"] = text.get('detailInfo').get("address")
            item["score"] = text.get('detailInfo').get("avgScore")
            item["telephone"] = text.get('detailInfo').get("phone")
            item["opentime"] = text.get('detailInfo').get("openTime")
            yield item
            print(item)
            time.sleep(random.random()*3)


















#
