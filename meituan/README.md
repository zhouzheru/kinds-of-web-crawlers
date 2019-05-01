
爬虫爬取美团各地美食，店铺信息。

由于没有对接代理，和cookies，爬到的内容很有限。

先访问各个城市，拿到城市对应的URL
![image1](https://raw.githubusercontent.com/zhouzheru/kinds-of-web-crawlers/master/meituan/meituan/spiders/1556676606(1).jpg)

然后访问对应URL，获取其页面上的店铺，页面最大限制是69页，每页15家店铺，这并不是所有的店铺，由于没有按照地区划分，只获取了那其中的69页店铺。

![image2](https://raw.githubusercontent.com/zhouzheru/kinds-of-web-crawlers/master/meituan/meituan/spiders/1556676629(1).jpg)

之后回去店铺URL，访问详情页,获取店铺的名字，开放时间，电话，地址。

![image3](https://raw.githubusercontent.com/zhouzheru/kinds-of-web-crawlers/master/meituan/meituan/spiders/1556676655(1).jpg)

最后 yield item 存入MongoDb

![image4](https://raw.githubusercontent.com/zhouzheru/kinds-of-web-crawlers/master/meituan/meituan/spiders/1556676075(1).jpg)

总的来说，难点在于URL 的构造和部分逻辑关系，由于资源有限，没有设置代理，私下设置代理时发现访问仍然302，如果全站爬需要对接代理池，COOKIES池
