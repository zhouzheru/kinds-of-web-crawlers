import requests
import json
import re
import time
from lxml import etree
import csv

class Avengers():

    with open("Avengers.csv","w")as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","comment","vote","time"])
    cookies = """ll="118171"; bid=L2H1_ogIlWA; _vwo_uuid_v2=DF6A79DC8F9F9D4848BB4835420B8AC2A|199151b95270e18d39107c7f94f7c3a6; __yadk_uid=0ndQ88ISQp48VLTRmnTw6LrRGeeC1jSt; douban-fav-remind=1; push_doumail_num=0; __utmv=30149280.13804; push_noty_num=0; douban-profile-remind=1; gr_user_id=b0568e35-f8e8-4e2d-b306-e438aa37a0a3; ps=y; __utmc=30149280; __utmz=30149280.1556596636.41.27.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1556596636.30.21.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1556599708%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DlHoDrq3bFV07i_j598DYg3wBkjwX2tZblLQJClCnC4WWXi5Q86mkjj09FBH1eKes%26wd%3D%26eqid%3Df54b980b000130ae000000035cc7c7f1%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.40774678.1550814918.1556596636.1556599708.42; __utma=223695111.842018130.1550814971.1556596636.1556599708.31; __utmb=223695111.0.10.1556599708; __utmb=30149280.1.10.1556599708; dbcl2="138048749:c6nYu7aXoek"; ck=I1LP; RT=r=https%3A%2F%2Fmovie.douban.com%2Fsubject%2F26100958%2Fcomments%3Fstart%3D480%26limit%3D20%26sort%3Dnew_score%26status%3DP&ul=1556601847444&hd=1556601847871; _pk_id.100001.4cf6=acbafa7d8b2eecb8.1550814971.29.1556602068.1556597022."""
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}

    def Ironman(self,page):

        url = "https://movie.douban.com/subject/26100958/comments?start={}&limit=20&sort=new_score&status=P".format(page)

        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        text = requests.get(url,headers = headers,cookies = self.cookies).text
        response = etree.HTML(text)
        div_list = response.xpath("//div[@class='mod-bd']//div[@class='comment-item']")
        # print(div_list)

        for div in div_list:
            item = {}
            item["name"] = div.xpath('./div[1]/a/@title')[0]
            item["score"] =div.xpath("./div[2]/h3/span[2]/span[2]/@class")[0]
            item["comment"] =  div.xpath("./div[2]/p/span//text()")[0]
            item["votes"] = div.xpath("./div[2]/h3/span[1]/span[1]//text()")[0]
            try:
                item["time"]=div.xpath("./div[2]/h3/span[2]/span[3]//text()")[0].strip()
            except:
                item["time"] = '\\'

            yield item


    def AC(self,item):
        with open("Avengers.csv","a",encoding="utf8",newline="") as f:
            writer = csv.writer(f)
            for each in item:
                writer.writerow([each["name"],each["score"],each["comment"],each["votes"],each["time"]])

if __name__ == '__main__':
    for page in range(0,500,20):
        A =Avengers()
        s =A.Ironman(page)
        A.AC(s)
        print("正在写入第{}页".format(int(page/20)))
        time.sleep(2)
