import requests
import json
import re
import time


class Weibo:
    username = input("请输入微博账号：")
    pwd = input("请输入微博密码")

    def __init__(self):
        login_url = "https://passport.weibo.cn/sso/login"
        self.login_url  = login_url#初始登录界面 ，需要模拟登陆获取cookies
        self.headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
                        "Referer":'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2Fbeta'}
        self.session = requests.Session()




    def login(self):
                        #账号密码登陆#
        data = {
      'username': self.username,
      'password': self.pwd,
      'savestate': '1',
      'r': 'https://m.weibo.cn/beta',
      'ec': '0',
      'pagerefer': 'https://m.weibo.cn/login?backURL=https%253A%252F%252Fm.weibo.cn%252Fbeta',
      'entry': 'mweibo',
      'wentry': '',
      'loginfrom': '',
      'client_id': '',
      'code': '',
      'qq': '',
      'mainpageflag': '1',
      'hff': '',
      'hfp': ''}

        response = requests.post(url=self.login_url,headers = self.headers,data = data)
        cookies = requests.utils.dict_from_cookiejar(response.cookies)

        return cookies

    def get_my_weibo(self,cookies):

        response =self.session.get(url=my_url,headers = self.headers,cookies = cookies)
        text = json.loads(response.text)
        cards =text.get("data").get("cards")

        for card in cards:
            item = {}
            if card.get("mblog"):
                item["create_time"] = card.get("mblog").get("created_at") #创建微博的时间
                item["content"] = card.get("mblog").get("raw_text") #内容
                if bool(item["content"]) == False: #原创微博在text中
                    item["content"] = card.get("mblog").get("text")
                item["content"] = re.sub("<.*?>","",item["content"]) #内容处理
                print(item)







if __name__ == '__main__':
    for i in range(1,50): #具体多少页 ，看个人
        my_url = "https://m.weibo.cn/api/container/getIndex?containerid=2304135360652011_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={}".format(i) #个人微博URL,AKAX
        wb = Weibo()
        c=wb.login()
        wb.get_my_weibo(c)
        time.sleep(5)


















# ~!
