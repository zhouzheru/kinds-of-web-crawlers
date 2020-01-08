from urllib.parse import unquote
import os
from urllib.request import urlretrieve
import time
import requests
import json
import threading
import queue


class Producer(threading.Thread):
    def __init__(self,page_queue,image_queue,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.image_queue = image_queue

    def extract_images(self,data):
        images = []
        for x in range(1,9):
            image_url = unquote(data.get("sProdImgNo_{}".format(x))).replace("200",'0')
            images.append(image_url)
        return images

    def run(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
        while not self.page_queue.empty():
            page_url = self.page_queue.get()
            resp = requests.get(page_url,headers = headers).text
            text = json.loads(resp)
            Lists = text.get("List")
            image_lists = []
            for each in Lists:
                image_list = []
                name =unquote(each.get("sProdName")).replace("1:1","").strip()
                image_url = self.extract_images(each)
                dir_path = os.path.join("images", name)
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                for index,url in enumerate(image_url):
                    # print(name,index+1,url)

                    self.image_queue.put({"name":name,"index":index,"url":url})
        print("###########线程{}执行完毕！###########".format(threading.current_thread().name))



class Consumer(threading.Thread):
    def __init__(self,image_queue,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.image_queue = image_queue

    def run(self):
        while True:
            try:
                image_obj = self.image_queue.get(timeout=5)
                dirname = image_obj.get("name")
                img_url = image_obj.get('url')
                index = image_obj.get("index")
                # print(dirname)
                # 如果不存在这个文件夹，就创建一个文件夹
                dir_path = os.path.join("images",dirname)
                # print(dir_path)

                s = os.path.join(dir_path, "{}.jpg".format(index+1))
                # print(s)
                # print(img_url)
                urlretrieve(img_url, s)
                print(s + "下载完成！")
            except:
                print("所有内容已下载完成！！！！！！！！")
                break
                # print(s)


def main():
    page_queue = queue.Queue(20)
    image_queue =queue.Queue(1200)
    for x in range(0,1):
        page_url = "https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={page}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1554446236641".format(page=x)
        page_queue.put(page_url)


    for i in range(5):
        th = Producer(page_queue,image_queue,name = "生产者线程{}号。".format(i))
        th.start()

    for i in range(5):
        time.sleep(2)
        th = Consumer(image_queue ,name = "消费者线程{}号。".format(i))
        th.start()
if __name__ == '__main__':
    main()
