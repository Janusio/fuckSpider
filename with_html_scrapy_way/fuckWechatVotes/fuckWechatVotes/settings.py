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

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

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
# ITEM_PIPELINES = {
#    'fuckWechatVotes.pipelines.FuckwechatvotesPipeline': 300,
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
COOKIES = "SUV=00295556ABD6F0C75AF1C57CFD2A1338; IPLOC=CN5101; SUID=391158DA4F18910A000000005AF64DA0; SNUID=70ED2F2B5D58310718B721405E87C24D; ABTEST=0|1529808413|v1; weixinIndexVisited=1; JSESSIONID=aaaJRyBGqjvsU_z9TUlnw; sct=5; ppinf=5|1529905109|1531114709|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OkphbnVzfGNydDoxMDoxNTI5OTA1MTA5fHJlZm5pY2s6NTpKYW51c3x1c2VyaWQ6NDQ6bzl0Mmx1R29FaU1aR0UwOWJ3UnZ2WXVXVGMzQUB3ZWl4aW4uc29odS5jb218; pprdig=wQAwZ7ViT0BGJO9R-G-zWc3e-O_Xyq5LmdD3Cli_hbE--v4nZmI3F6Jpzuot9y4HRU3RSy6ZU6bUZ0TplzQq90_YtMK2QD1xuV6tdkUAAY90_sQbGVJaNP2ffQuLzLveLzYAtBcTY91IoMBqwDOuzn6Iyre7Hm5PW1RGiHKi6so; sgid=23-35698767-AVswf9UwtN5m9rdvwSEUfGw; ppmdig=15299051100000008e19c04fcc3fdf9024571c2f93ba1834"
