# -*- coding:utf-8 -*-
# Author: Neng Qi
from scrapy import cmdline

cmdline.execute('scrapy crawl wechatVoteSpider -a k=艺术投票'.split())
