import requests
import json
from lxml import etree
import re
from pymongo import MongoClient

class Wx_News(object):
    def __init__(self):
        url = "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MTI0MDU3NDYwMQ==&f=json&offset={}&count=10&is_ok=1&scene=126&uin=777&key=777&pass_ticket=NLZEohgmMNUf5MC6%2BYVblzVuF9zXMDlSU4hpU6ZN7e0R055zQr76ufP82KMzsokB&wxtoken=&appmsg_token=1007_9jnhmoKmGgyansWNXY_pPlCUZZPHX0m5h4bXaA~~&x5=0&f=json".format(offset)
        url_sample=""
        self.url = url
        self.session = requests.Session()
        cookies = """
        devicetype=iOS12.2; lang=zh_CN; pass_ticket=NLZEohgmMNUf5MC6+YVblzVuF9zXMDlSU4hpU6ZN7e0R055zQr76ufP82KMzsokB; version=1700032a; wap_sid2=CLXW6s0KElxub200aFd3UWxIa3NIM3h0Z1p6emdXU0E0WDNxTEVNOWpWNlBqZFFnak82bmQtdGpDbENFQ0FkMUtNMDAzUVFvYmhodUJVZDRoZHRoTEJPeVloM3lWdThEQUFBfjDvmarmBTgNQJVO; wxuin=2847583029; wxtokenkey=777; rewardsn=; ts_uid=8846380392; pgv_pvid=8494402558; RK=SJqd6MTocG; ptcz=0ed4fae9d2265fb39d767b2bb015e5439e44478f004d54cf513d6c6a16af9ab3; pgv_pvi=4496419840; eas_sid=41h5p5W3p3P2O6n698O7b53489; sd_cookie_crttime=1550841826072; sd_userid=81711550841826072"""

        self.cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.strip().split(";")}
        self.headers = {"User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN'}
        self.client = MongoClient("localhost")
        self.db = self.client["yangshixinwen"]

    def News(self):


        s= self.session.get(self.url,headers = self.headers,cookies = self.cookies)
        text = json.loads(s.text)
        msg_list = json.loads(text.get("general_msg_list"))
        msg_list=msg_list.get("list")
        for each in msg_list:
            app_msg_ext_info=each.get("app_msg_ext_info")
            item = {}
            item["title"] = app_msg_ext_info.get("title")
            item["content_url"] = app_msg_ext_info.get("content_url").lstrip()
            if item["content_url"]: #防止有的新闻被删除但是占位导致获取不到URL
                print(item["content_url"])
                text = self.session.get(item["content_url"],headers = self.headers).text
                HTML = etree.HTML(text)
                try:
                    news =HTML.xpath("//div[@class='rich_media_content ']//text()")
                    item["news"]="".join(news).strip()
                    item["publish_time"] = re.findall('var publish_time = \"(.*?)\" \|\| \"\"',text,re.S)[0]
                except:
                    pass


                multi_app_msg_item_list =app_msg_ext_info.get("multi_app_msg_item_list")
                for each in multi_app_msg_item_list:
                    item1 = {}
                    item1["title"] = each.get("title")
                    item1["content_url"] = each.get("content_url").strip()
                    if item1["content_url"]:
                        text = self.session.get(item1["content_url"],headers = self.headers).text
                        HTML = etree.HTML(text)
                        try:
                            news =HTML.xpath("//div[@class='rich_media_content ']//text()")
                            item1["news"]="".join(news).strip()
                            item1["publish_time"] = re.findall('var publish_time = \"(.*?)\" \|\| \"\"',text,re.S)[0]
                            self.db["Wx_news"].insert(dict(item))
                            self.db["Wx_news"].insert(dict(item1))
                            # print(item)
                            # print(item1)
                        except:
                            pass





if __name__ == '__main__':
    for i in range(0,100000,10): #具体页数自己确定，访问到一定数量就获取不到内容了，会显示操作频繁，扫码手机阅览
        offset =5000
        s=Wx_News()
        s.News()
        print("第{}页已经下载完成".format(int(offset/10)))
