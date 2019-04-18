import requests
from  urllib.parse import urlencode
from lxml import etree
import csv

class doubanMoive:
    cookies = 'll="118171"; bid=L2H1_ogIlWA; _vwo_uuid_v2=DF6A79DC8F9F9D4848BB4835420B8AC2A|199151b95270e18d39107c7f94f7c3a6; __yadk_uid=0ndQ88ISQp48VLTRmnTw6LrRGeeC1jSt; douban-fav-remind=1; ct=y; push_doumail_num=0; __utmv=30149280.13804; push_noty_num=0; douban-profile-remind=1; __utmc=30149280; __utmz=30149280.1553668446.33.22.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1553674260%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E6%2596%25B0%25E4%25B8%2596%25E7%2595%258C%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.40774678.1550814918.1553668446.1553674261.34; __utmb=30149280.1.10.1553674261; __utma=223695111.842018130.1550814971.1553668460.1553674275.27; __utmb=223695111.0.10.1553674275; __utmz=223695111.1553674275.27.19.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; ap_v=0,6.0; _pk_id.100001.4cf6=acbafa7d8b2eecb8.1550814971.25.1553675765.1553670195.; dbcl2="138048749:vMzVhg6oOaI"'
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
    Session = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}


    def url_page(self,page):
        base_url ='https://movie.douban.com/subject/10437779/comments?'


        params = {'start':page,
                    'limit':'20',
                    "sort":'new_score',
                    "status":'P'}
        url  =base_url+urlencode(params)

        return url

    def get_Info(self,url):

        response = self.Session.get(url=url,headers = self.headers,cookies = self.cookies)
        text  =response.text
        response = etree.HTML(text)
        hrefs = response.xpath("//div[@class='mod-bd']/div[@class='comment-item']")
        s=[]
        for href in hrefs:

            item={}
            item["用户ID"] = href.xpath("./div[@class='comment']/h3/span[2]/a/text()")[0]
            item['stars'] = href.xpath("./div[@class='comment']/h3/span[2]/span[2]/@class")[0]
            if item["stars"] == 'allstar50 rating':
                item["stars"] = '5 星'
            elif item["stars"] == 'allstar40 rating':
                item["stars"] = '4 星'
            elif item["stars"] == 'allstar30 rating':
                item["stars"] = '3 星'
            elif item["stars"] == 'allstar20 rating':
                item["stars"] == '2 星'
            else:
                item["stars"] = "1 星"
            item["评论"] = href.xpath("./div[@class='comment']/p/span[@class='short']/text()")[0]
            s.append(item)
        return s

    def save_to_file(self,s):
        with open('新世界.csv','a',encoding = 'utf8',newline='') as f:
            writer = csv.writer(f)

            for i in range(len(s)):
                writer.writerow([s[i].get("用户ID"),s[i].get("stars"),s[i].get("评论")])



Moive = doubanMoive()
for i in range(20,480,20):
    url=Moive.url_page(i)
    s = Moive.get_Info(url)
    print("正在下载第{}页.....................".format(int(i/20)))
    Moive.save_to_file(s)
