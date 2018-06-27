# -*- coding:utf-8 -*-
# Author: Neng Qi
from scrapy import cmdline

cmdline.execute('scrapy crawl wechatVoteSpider -a k=画画投票'.split())
