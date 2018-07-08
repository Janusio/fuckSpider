# -*- coding: utf-8 -*-

# Scrapy settings for fuckAiHome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'fuckAiHome'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5467.400 QQBrowser/10.1.1503.400'
SPIDER_MODULES = ['fuckAiHome.spiders']
NEWSPIDER_MODULE = 'fuckAiHome.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fuckAiHome (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 8
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

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
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'fuckAiHome.middlewares.FuckaihomeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'fuckAiHome.middlewares.MyCustomDownloaderMiddleware': 543,
#}
EXTENSIONS = {
   'scrapy.extensions.memusage.MemoryUsage': None,
}
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'fuckAiHome.pipelines.FuckaihomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
COOKIESEEEE="TYCID=80ea5440814411e88171490ca18f11d1; undefined=80ea5440814411e88171490ca18f11d1; ssuid=5236386956; RTYCID=ba66ddf781c74ba8a4b72dc35daba93e; aliyungf_tc=AQAAABW/yH3FfAkA9rdydiMhtzXhq505; csrfToken=QJ7sUSKYY7iX55aNE0CSEOgC; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1530899192,1530943077; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQ4MjIxMjgyMCIsImlhdCI6MTUzMTAwMTExOSwiZXhwIjoxNTQ2NTUzMTE5fQ.UKJUGK_7bF6B_lHsyBABxq_SwJv5XEh5u1PtssY4EqYGwuXcZMH9fxJW_eo_oTNdFMbTqs2wLu0aMjCH9bvmXQ%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218482212820%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQ4MjIxMjgyMCIsImlhdCI6MTUzMTAwMTExOSwiZXhwIjoxNTQ2NTUzMTE5fQ.UKJUGK_7bF6B_lHsyBABxq_SwJv5XEh5u1PtssY4EqYGwuXcZMH9fxJW_eo_oTNdFMbTqs2wLu0aMjCH9bvmXQ; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1531001133"
COOKIES="aliyungf_tc=AQAAAMNiOHA7fQkAGrZydnMLWR2EVbe7; csrfToken=rkWxQKFdQnvNFcUP6lV7gRT2; TYCID=f52a477082cf11e889a8e5f8bd112cda; undefined=f52a477082cf11e889a8e5f8bd112cda; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1531069036; ssuid=6618825072; token=40a412e946d14d5fb620ae91a75801c0; _utm=577f4a64653b4065b8035cd53b561760; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQ4MjIxMjgyMCIsImlhdCI6MTUzMTA2OTEwNywiZXhwIjoxNTQ2NjIxMTA3fQ.d8jIzxf_ULwO4W8hGcBkEDeTWAM5SUFfJ2ffBIxlTxqGKMtIsglwjYfwMProiMcuuc8hlZlvnqBn_SSIBxfwrw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218482212820%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQ4MjIxMjgyMCIsImlhdCI6MTUzMTA2OTEwNywiZXhwIjoxNTQ2NjIxMTA3fQ.d8jIzxf_ULwO4W8hGcBkEDeTWAM5SUFfJ2ffBIxlTxqGKMtIsglwjYfwMProiMcuuc8hlZlvnqBn_SSIBxfwrw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1531069131"