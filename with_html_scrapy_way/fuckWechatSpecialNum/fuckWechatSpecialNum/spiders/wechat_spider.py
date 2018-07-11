# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from with_html_scrapy_way.fuckWechatSpecialNum.fuckWechatSpecialNum.items import *
class WechatSpiderSpider(scrapy.Spider):
    name = 'wechat_spider'
    allowed_domains = ['weixin.sogou.com', 'mp.weixin.qq.com']
    start_urls = []
    public_query_url = 'http://weixin.sogou.com/weixin?query={keyword}&_sug_type_=&s_from=input&_sug_=n&type=1&page=&ie=utf8'

    def start_requests(self):
        with open("C:/Users/neng.qi/PycharmProjects/fuckSpider/with_html_scrapy_way/fuckWechatSpecialNum/fuckWechatSpecialNum/spiders/wxdyh.txt",encoding="UTF-8") as f:
            for line in f:
                per_public=line.rstrip()
                per_public_list=per_public.split(',')
                name=per_public_list[0]
                num=per_public_list[1]
                url=self.public_query_url.format(keyword=num)
                yield Request(url=url,meta={"name":name,"num":num})
    def parse(self, response):
        item=WechatNumItem()
        item['name']=response.meta["name"]
        item['id']=response.meta["num"]
        url_xpath=response.xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/@href')
        if url_xpath:
            url=url_xpath.extract()[0]
            item['url']=url
            yield item

