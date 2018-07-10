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
# USER_AGENT = 'fuckAiHome (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
ITEM_PIPELINES = {
   # 'fuckWechatVotes.pipelines.FuckwechatvotesPipeline': 300,
   'fuckAiHome.pipelines.FuckaihomeDbPipeline': 300,
}
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
#    'fuckAiHome.middlewares.FuckaihomeSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'fuckAiHome.middlewares.MyCustomDownloaderMiddleware': 543,
# }
EXTENSIONS = {
    'scrapy.extensions.memusage.MemoryUsage': None,
}
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'fuckAiHome.pipelines.FuckaihomePipeline': 300,
# }

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
COOKIESEEEE = "TYCID=80ea5440814411e88171490ca18f11d1; undefined=80ea5440814411e88171490ca18f11d1; ssuid=5236386956; RTYCID=ba66ddf781c74ba8a4b72dc35daba93e; aliyungf_tc=AQAAABW/yH3FfAkA9rdydiMhtzXhq505; csrfToken=QJ7sUSKYY7iX55aNE0CSEOgC; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1530899192,1530943077; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQ4MjIxMjgyMCIsImlhdCI6MTUzMTAwMTExOSwiZXhwIjoxNTQ2NTUzMTE5fQ.UKJUGK_7bF6B_lHsyBABxq_SwJv5XEh5u1PtssY4EqYGwuXcZMH9fxJW_eo_oTNdFMbTqs2wLu0aMjCH9bvmXQ%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218482212820%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQ4MjIxMjgyMCIsImlhdCI6MTUzMTAwMTExOSwiZXhwIjoxNTQ2NTUzMTE5fQ.UKJUGK_7bF6B_lHsyBABxq_SwJv5XEh5u1PtssY4EqYGwuXcZMH9fxJW_eo_oTNdFMbTqs2wLu0aMjCH9bvmXQ; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1531001133"
COOKIES = "aliyungf_tc=AQAAAAdRKR0azA4AZD+WtlIxIQ4RclUc; csrfToken=HV119cZfia4bjLaY4l5RdB-8; TYCID=848ab450833811e887f2cf6e044ddc15; undefined=848ab450833811e887f2cf6e044ddc15; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1531113944; ssuid=3150529488; token=beeea4b5c3634edb86495ec192de2bd4; _utm=2975074fe13a45fba6ede5ae6a4d1370; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQ4MjIxMjgyMCIsImlhdCI6MTUzMTExMzk5OSwiZXhwIjoxNTQ2NjY1OTk5fQ.BRrHVB3gcEANFEePZUCXi8XaA7WbK38EFE0XsUsHkufzDR5sBnWjmOkq1LlTPpgRs29CYSkFm851EH-ekpbLIg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218482212820%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQ4MjIxMjgyMCIsImlhdCI6MTUzMTExMzk5OSwiZXhwIjoxNTQ2NjY1OTk5fQ.BRrHVB3gcEANFEePZUCXi8XaA7WbK38EFE0XsUsHkufzDR5sBnWjmOkq1LlTPpgRs29CYSkFm851EH-ekpbLIg; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1531114102"
COOKIESQIXIN = "channel=baidu; Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1531193708; cookieShowLoginTip=1; sid=s%3ACuU3LiBKI5u2Dv2P18NTftIWMhMbr2nw.ze0BkOArz5AOpYm30FthnFt40mnk9vBdmb621o0Pn9Y; Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1531196274; _zg=%7B%22uuid%22%3A%20%221648241cc30138-0499328f36b061-335f4f76-1fa400-1648241cc3199d%22%2C%22sid%22%3A%201531196158.377%2C%22updated%22%3A%201531196275.086%2C%22info%22%3A%201531193707573%2C%22cuid%22%3A%20%2228b3ffd7-6b34-4701-80bb-07d04eca5e6d%22%7D; responseTimeline=49"
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'codingatwill'
MYSQL_USER = 'root'
MYSQL_PASSWD = '1314'
