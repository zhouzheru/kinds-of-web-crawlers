import requests
from lxml import etree
from urllib.parse import urlencode

def douban(number):
    url = 'https://accounts.douban.com/j/mobile/login/request_phone_code'


    session = requests.Session()
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',}
    data = {'ck':'',
    "area_code":"+86",
    "number":number}
    response = session.post(url,headers = headers,data = data)

    s = input("请输入获取的验证码:")
    new_url = 'https://accounts.douban.com/j/mobile/login/verify_phone_code'
    new_data ={"ck":'',
                'area_code':"+86",
                'number':'15706291693',
                'code':s,
                "remember":"false",
                "ticket":''}
    response = session.post(new_url,headers = headers,data =new_data )

    print("以下是你想看的电影：")
    for num in range(0,45,15):
        base_url = 'https://movie.douban.com/people/138048749/wish?start='+str(num)+'&'
        params = {'sort':'time',
                "rating":'all',
                'filter':'all',
                'mode':'grid'}
        url  =base_url+urlencode(params)
        result = session.get(url,headers =headers).text
        result = etree.HTML(result)
        wish = result.xpath('//li[@class = "title"]/a/em/text()')
        for i in wish:
            print(i,end = "\n")
    print('------------------------------------------------分割线------------------------------------------------------------------------------------------')
    print('以下是你看过的电影：')
    for num in range(0,45,15):
        base_url = 'https://movie.douban.com/people/138048749/collect?start='+str(num)+'&'
        params = {'sort':'time',
                "rating":'all',
                'filter':'all',
                'mode':'grid'}
        url  =base_url+urlencode(params)
        result = session.get(url,headers =headers).text
        result = etree.HTML(result)
        wish = result.xpath('//li[@class = "title"]/a/em/text()')
        for i in wish:
            print(i,end = "\n")
douban(input("请输入你的手机号："))
