# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from with_html_scrapy_way.fuckAiHome.fuckAiHome.utils.transcookie import *
from scrapy.conf import settings
from with_html_scrapy_way.fuckAiHome.fuckAiHome.items import *


class AiHomeQixinbaoSpiderSpider(scrapy.Spider):
    name = 'ai_home_qixinbao_spider'
    allowed_domains = ['qixin.com']
    start_urls = []
    base_url_main = 'http://www.qixin.com'
    base_url = 'http://www.qixin.com/search?area.city=5101&area.province=51&key=%E6%99%BA%E8%83%BD%E5%AE%B6%E5%B1%85&page={}'
    trans = transCookie(settings['COOKIESQIXIN'])
    cookies = trans.stringToDict()
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5408.400 QQBrowser/10.1.1430.400'
    }

    def start_requests(self):
        for ii in range(1, 11):
            yield Request(url=self.base_url.format(ii), cookies=self.cookies, headers=self.headers)

    def parse(self, response):
        per_company_url_list = response.xpath('/html/body/div[5]/div/div[1]/div[3]/div[2]/div')
        if per_company_url_list:
            for ii in per_company_url_list:
                per_tel=ii.xpath('div[2]/div[1]/div[3]/span[1]/text()')
                c_tel=''
                if per_tel:
                    c_tel=per_tel.extract()[0]
                c_email=''
                per_email=ii.xpath('div[2]/div[1]/div[3]/span[2]/a/text()')
                if per_email:
                    c_email=per_email.extract()[0]
                per_url = ii.xpath('div[2]/div[1]/div[1]/a/@href')
                if per_url:
                    yield Request(url=(self.base_url_main+per_url.extract()[0]), callback=self.parse_per_company, cookies=self.cookies,
                                  headers=self.headers,meta={'c_tel': c_tel, 'c_email': c_email})

    def parse_per_company(self, response):
        item = CompangItem()
        item['c_address'] = ""
        item['c_description'] = ""
        item['c_email'] = response.meta['c_email']
        item['c_hangye'] = ""
        item['c_leg_people'] = ""
        item['c_name'] = ""
        item['c_regis_address'] = ""
        item['c_regis_money'] = ""
        item['c_regis_time'] = ""
        item['c_tel'] = response.meta['c_tel']
        item['c_jingyingfanwei'] = ""
        item['c_id'] = response.url
        company_info_container = response.xpath('/html/body/div[6]')
        if company_info_container:
            c_address = company_info_container.xpath('//*[@id="icinfo"]/table/tbody/tr[7]/td[2]/text()')
            if c_address:
                item['c_address'] = c_address.extract()[0]
            c_regis_time = company_info_container.xpath('//*[@id="icinfo"]/table/tbody/tr[3]/td[4]/text()')
            if c_regis_time:
                item['c_regis_time'] = c_regis_time.extract()[0]
            c_hangye = company_info_container.xpath('//*[@id="icinfo"]/table/tbody/tr[3]/td[2]/text()')
            if c_hangye:
                item['c_hangye'] = c_hangye.extract()[0]
            c_leg_people = company_info_container.xpath('//*[@id="icinfo"]/table/tbody/tr[5]/td[2]/a[1]/text()')
            if c_leg_people:
                item['c_leg_people'] = c_leg_people.extract()[0]
            c_regis_money = company_info_container.xpath('//*[@id="icinfo"]/table/tbody/tr[6]/td[2]/text()')
            if c_regis_money:
                item['c_regis_money'] = c_regis_money.extract()[0]
            c_jingyingfanwei = company_info_container.xpath('//*[@id="icinfo"]/table/tbody/tr[8]/td[2]/text()')
            if c_jingyingfanwei:
                item['c_jingyingfanwei'] = c_jingyingfanwei.extract()[0]
        item['c_product'] = ""
        c_product = response.xpath('//*[@id="entcard"]/div/div/div/text()')
        if c_product:
            item['c_product'] = str(c_product.extract()[0])
        # c_email = response.xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/a/text()')
        # if c_email:
        #     item['c_email'] = c_email.extract()[0]
        c_name = response.xpath('/html/body/div[3]/div/div/div[2]/div/div[1]/h3/text()')
        if c_name:
            item['c_name'] = c_name.extract()[0]
        c_regis_address = response.xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[1]/div[4]/div/div[2]/text()')
        if c_regis_address:
            item['c_regis_address'] = c_regis_address.extract()[0]
        # c_tel = response.xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/span/text()')
        # if c_tel:
        #     item['c_tel'] = c_tel.extract()[0]
        yield item
    # item['c_address'],
    # item['c_description'],
    # item['c_email'], item['c_hangye'],
    # item['c_id'], item['c_leg_people'],
    # item['c_name'], str(item['c_product']),
    # item['c_regis_address'], item['c_regis_money'],
    # time_str_str, item['c_tel'], item['c_jingyingfanwei']
