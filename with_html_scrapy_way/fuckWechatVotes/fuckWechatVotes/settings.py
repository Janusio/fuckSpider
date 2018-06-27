# -*- coding: utf-8 -*-

# Scrapy settings for fuckWechatVotes project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'fuckWechatVotes'

SPIDER_MODULES = ['fuckWechatVotes.spiders']
NEWSPIDER_MODULE = 'fuckWechatVotes.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'fuckWechatVotes (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 不遵守Robot协议

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
# 　　custom_settings = { 'DOWNLOAD_DELAY': 0.2, 'CONCURRENT_REQUESTS_PER_IP': 4, 'DOWNLOADER_MIDDLEWARES': {}, }
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'fuckWechatVotes.middlewares.FuckwechatvotesSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'fuckWechatVotes.middlewares.MyCustomDownloaderMiddleware': 543,
   # 'fuckWechatVotes.middlewares.ProxyMiddleWare': 125
}
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400'
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }
EXTENSIONS = {
   'scrapy.extensions.memusage.MemoryUsage': None,
}
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'fuckWechatVotes.pipelines.FuckwechatvotesPipeline': 300,
   'fuckWechatVotes.pipelines.DBPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# COOKIES = "ABTEST=0|1530073841|v1; IPLOC=CN5101; SUID=B8B072764A42910A000000005B3312F1; SUID=B8B072763320910A000000005B3312F1; weixinIndexVisited=1; SUV=001F253D7672B0B85B3312F6CA259194; ppinf=5|1530073860|1531283460|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OkphbnVzfGNydDoxMDoxNTMwMDczODYwfHJlZm5pY2s6NTpKYW51c3x1c2VyaWQ6NDQ6bzl0Mmx1R29FaU1aR0UwOWJ3UnZ2WXVXVGMzQUB3ZWl4aW4uc29odS5jb218; pprdig=JgJWXZSd5qyjR-7Ft_M-x694LKTYP8MXaD8AD-Qo2y1-1yKldBhaYGxgwLzQ8L-n519Ye98zAMjjFH2WmROk-KbE8BCrx5oR1OJqWv-3K5dMHSDvKlA1aOZZ7LWhdRQzNi4Altau7CKgewLz2tPeG7IQZjbkSrGGdIb7l17FN-M; sgid=23-35698767-AVszEwNEoAGasSN8Ga0RtCQ; ppmdig=153007386000000060fb46dea826b38eb31290a2738d61c5; sct=1; SNUID=0C05C6C2B5B0DA2DA1398223B5644FD8; JSESSIONID=aaa7yJ2s0Nkr9chzhR7qw"
COOKIES = "ABTEST=0|1530104183|v1; IPLOC=CN5101; SUID=B8B072764A42910A000000005B338977; SUID=B8B072763320910A000000005B338977; weixinIndexVisited=1; SUV=00FD0B897672B0B85B338978939D6711; sct=1; SNUID=151EDFDBAEA8C1318A41BEE4AEE94BA7; JSESSIONID=aaaQbTT7JAFeb5ZNUS7qw; ppinf=5|1530104212|1531313812|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OkphbnVzfGNydDoxMDoxNTMwMTA0MjEyfHJlZm5pY2s6NTpKYW51c3x1c2VyaWQ6NDQ6bzl0Mmx1R29FaU1aR0UwOWJ3UnZ2WXVXVGMzQUB3ZWl4aW4uc29odS5jb218; pprdig=qXXjca3d8HBybsP3I3-q0Xrhxrjc0AYzmZcjnHOgC5se83v4dmupTTqcM5LsWQrkkc8CEt8zx00H2DI_tWYsEqfOCFlluQO-rDA9cBLv1Iy8WEcG9vwn_MZAZIfFdtYrcJ00tzdng0G5AZTq1fE246pPIO2uXc4ngLw005nIY5E; sgid=23-35698767-AVsziaZTBM0FcZSrTIuB8xiao; ppmdig=1530104213000000e7927084f08bc6d29a34eaf35bd79e70"
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'codingatwill'
MYSQL_USER = 'root'
MYSQL_PASSWD = '1314'