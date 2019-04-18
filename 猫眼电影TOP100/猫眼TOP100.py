import requests
import re
def get_onepage(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return response.text
    else:
        return None
def main():
    html = get_onepage(url)
    return html

def parse_onepage(html):
    tup =[]
    partent = re.compile('<dd>.*?board-index-.*?">(.*?)</i>\
.*?data-src="(.*?)"\
.*?class="name".*?title="(.*?)".*?</a></p>\
.*?"star">(.*?)</p>.*?="releasetime">(.*?)</p>\
.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i></p>',re.S)

    items = re.findall(partent,html)
    for item in items:
        txt=("排名:"+item[0],"图片网址:"+item[1],"电影:"+item[2],\
item[3].strip(),item[4],"评分:",item[5]+item[6])
        content = ",".join(tuple(txt))
        save(content+"\n")
        

    
def save(content):
    f= open("猫眼top100.txt","a")
    f.write(content)
i=0
while i <=90:
    url = 'https://maoyan.com/board/4?offset='+str(i)
    html = main()
    content = parse_onepage(html)
    i+=10
   
