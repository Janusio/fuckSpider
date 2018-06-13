# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['www.fang.com']
    start_urls = ['http://www.fang.com/']

    def parse(self, response):
        pass
