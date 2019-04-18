from lxml import etree
import requests
import csv
import time


def get_info(url):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    contents = requests.get(url,headers = headers)
    text = contents.text
    return text
def parse_info(text):
    html = etree.HTML(text)
    name = html.xpath('//span[@class="comment-info"]/a/text()')
    remark = html.xpath('//p/span[@class="short"]/text()')
    dianzan = html.xpath('//span[@class="votes"]/text()')
    stars =html.xpath("//span[@class='comment-info']/span[last()-1]/@class")
    remarktime = html.xpath('//span[@class = "comment-time "]/@title')
    return name,remark,dianzan,stars,remarktime
list1 = []

def write_to_file(name,remark,dianzan,stars,remarktime):
    with open("DMKJ.csv",'w',encoding='utf-8',newline='',errors='ignore') as f:
        writer = csv.writer(f)
        writer.writerow(['昵称','星数','点赞数','评价','评价时间'])
        for i in range(len(name)):
            list1.append([name[i],stars[i],dianzan[i],remark[i],remarktime[i]])
        for each in list1:
            writer.writerow(each)
for i in range(0,100,20):
    url="https://movie.douban.com/subject/3541415/comments?start="+str(i)+'&limit=20&sort=new_score&status=P'

    text=get_info(url)
    name,remark,dianzan,stars,remarktime=parse_info(text)
    write_to_file(name,remark,dianzan,stars,remarktime)
