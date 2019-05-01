# -*- coding: utf-8 -*-

# Scrapy settings for meituan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meituan'

SPIDER_MODULES = ['meituan.spiders']
NEWSPIDER_MODULE = 'meituan.spiders'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
LOG_LEVEL  = 'WARNING'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meituan (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# MEDIA_ALLOW_REDIRECTS =False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

MONGO_URL = "localhost"
MONGO_DB = 'MeiTuan'
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# # TOKEN = ["eJyFT11vqkAU/C/7KpHdFRbxDS8KGD+KArfY9AHpAisuWBYVafrfu03b5N6nJieZOXMmkzlvoPFewARBaEKogCttwASgIRwSoIBWyIuuEx2bOhojYiog/V/DBCvg0EQ2mDyhESEK0uHzp7KVwpdikPGz8g/FmpxPjyctoGjbs5ioalokVZ7RKu9YUg05Ze1FYlpzVXJRMFXW+d0LZC4PZK7E8huTb2x/9pX8UKYJlleS0cXtdAzQxupnfkEHu9trNHKpF7GBz3Z1GMJHxyoDbGzw0vRGIi3DS6l12hkOwnvoWkt7Hlyh+WDgcOpQN+HzLo5VzdVUy6N9lrlqtsbqoZGdV/5qajL70FU9gzzmy3u7vTOfrGe9vQ3oCjd/90VAaU0u8E+8uPX9Bjq+W5+asGtNZOQCeeVsjMfIpzE+tFs8c8p5xZe4T/VwVOvarYk6tufrV+tRrbg47e+9MDa2s0vE4mVwnuYdFtG8fqDHKz6SdSjOmannqTeFRgPePwCfsqBB",
# "eJyFT01vozAU/C++BsXGYAi5kSUBonyUBLMlqx4INeAQIMUkIVT739dVW2n3tNKTZt680WjeO2j9VzBVEbIQUsCNtWAK1DEaG0ABnZAXQgyCLYJ1i2gKSP/RCNInCji2kQOmv1TNMBSVoJcPZSeFT8U0Ji/KXxTrcj48vrSAousuYgphWiR1nrE673lSjyvGu6vEtKmg5KLgUNb5vxfI3CqUuRLLL0y+sPve1/JDmSZ4XkvGlvfzKVS39jAPCjba398izWN+xEcB3zeUomfXLkNsbvHK8jWRlvRa6r1+QSP6oJ69chbhDVlPJqYzl3lJtejjGOqeDm2fDVnmwWyD4bGVndfBemZx59jXA0dVXK0e3e7BA2MzH5xdyNa4/XkoQsYa44p+xMv7MGyRG3jNuaV9Z6lmLlS/nE/wRA1YjI/dDs/dclFXKzykhGoN0e9t1PNDtXmzn2FdifPhMQhz67j7RCxfR5dZ3mMRLZondrrhk7Gh4pJZJE/9GTJb8PsPm/KgPw==",
# 'eJyFT9tuozAU/Be/BsXG4Zo3siRAlEtJMFuy6gOhBhxiSDFJCNX++7pqK632ZaUjzZw5o9Gcd9AGr2CqImQjpIAbbcEUqGM0NoACOiEvum7o2NZ1bCFLAdk/mmkq4NjGLpj+UieGoag6evlQdlL4VEzDelH+oliT8+EJpAWUXXcRUwizMq2LnNZFz9J6zCnrrhKzhkPJRcmgrPN/L5C5PJK5EqsvTL+w+97X8kOZJlhRS0aX9/MpUrfOMA9LOtrf3+KJT4OYjUK2bwhBz55TRdjc4pUdTERWkWul9doFjciD+M7KXUQ3ZD+ZmMw86qd80ScJ1HwNOgEd8tyH+QbDYys7r8P1zGbusa8HhnjCV49u92ChsZkP7i6ia9z+PJQRpY1xRT+S5X0YtsgL/ebckr6zVbMQalDNLWypIU3wsdvhuVctar7CQ6aTSaNr9zbu2YFv3pxnWHNxPjwGYW5db5+K5evoMit6LOJF80RPN3wyNkRcclsvsmCGzBb8/gOt66BJ']

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'meituan.middlewares.MeituanSpiderMiddleware': 543,
#}
PROXIES_LIST =['https://111.79.188.240:6888', 'https://111.79.188.158:6888', 'https://111.79.188.162:6888', 'https://111.77.112.59:6888', 'https://111.79.188.210:6888', 'https://111.79.189.35:6888', 'https://111.77.115.242:6888', 'https://111.79.188.183:6888', 'https://111.79.189.224:6888', 'https://111.79.188.62:6888', 'https://111.77.114.115:6888', 'https://111.79.188.36:6888', 'https://111.79.188.77:6888', 'https://111.79.188.177:6888', 'https://111.77.115.135:6888', 'https://111.79.188.252:6888', 'https://111.79.188.145:6888', 'https://111.79.188.237:6888', 'https://111.77.114.132:6888', 'https://111.77.115.153:6888']

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'meituan.middlewares.ProxyMiddleware': 543,
#    # "meituan.middlewares.Checkproxies":544
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'meituan.pipelines.MongoDbpipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
