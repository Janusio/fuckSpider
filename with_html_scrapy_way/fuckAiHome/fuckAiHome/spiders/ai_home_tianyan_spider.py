# -*- coding: utf-8 -*-
import scrapy


class AiHomeTianyanSpiderSpider(scrapy.Spider):
    name = 'ai_home_tianyan_spider'
    allowed_domains = ['tianyancha.com']
    start_urls = ['http://tianyancha.com/']

    def parse(self, response):
        pass
