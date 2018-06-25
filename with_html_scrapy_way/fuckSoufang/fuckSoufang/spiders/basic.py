# -*- coding: utf-8 -*-
import scrapy
import re
import json


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['www.fang.com', 'soufunimg.com']
    start_urls = ['http://js.soufunimg.com/homepage/new/family/css/allcitys2018061301.js?v=2018061501']

    def parse(self, response):
        itessJson = "{"
        original = response.body.decode('utf-8')
        # itess=re.search(r'dsy.add\((.*)\);',original,re.M|re.I)
        # itess=re.match(r'dsy.add\((.*)\);',original,re.M|re.I)
        pattern = re.compile("dsy.add\((.*)\);")
        arry = pattern.findall(original)
        for arrr in arry:
            print(len(arrr))
    #
    # if itess:
    #     itessJson=re.sub(r',',':',itess.group(1),1)+"}"
    #     # print(json.loads(itessJson))
