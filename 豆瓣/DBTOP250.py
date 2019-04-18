import requests
import urllib.request
import  re


list1 = []
list2 = []
def get_onepage(url):

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
    result = requests.get(url,headers = headers)
    onepage = result.text
    return onepage

def parse_onepage(onepage):

    partent = re.compile('<img width="100".*?alt="(.*?)".*?src="(.*?)".*?class=""',re.S)
    content = re.findall(partent,onepage)
    for each in content:
        list1.append(each[1])
        list2.append(each[0])
    return list1
    return list2



def savefile(list1):
    for i in range(len(list1)):
        urllib.request.urlretrieve(list1[i],str(i+1)+"、"+list2[i]+".jpg")

j=0
while j <=225:
    url = "https://movie.douban.com/top250?start="+str(j)+"&filter="
    onepage=get_onepage(url)
    list1=parse_onepage(onepage)
    savefile(list1)
    j+=25
