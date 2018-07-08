# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from with_html_scrapy_way.fuckAiHome.fuckAiHome.utils.transcookie import *
from scrapy.conf import settings
from with_html_scrapy_way.fuckAiHome.fuckAiHome.items import *
import requests
from lxml import etree


class AiHomeTianyanSpiderSpider(scrapy.Spider):
    name = 'ai_home_tianyan_spider'
    allowed_domains = ['tianyancha.com']
    base_url = 'https://chengdu.tianyancha.com/search/p{}?key=%E6%99%BA%E8%83%BD%E5%AE%B6%E5%B1%85'
    start_urls = []
    base_product_url = 'https://www.tianyancha.com/pagination/product.xhtml?ps=&pn={}&id={}&_='
    trans = transCookie(settings['COOKIES'])
    cookies = trans.stringToDict()
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5467.400 QQBrowser/10.1.1503.400Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5467.400 QQBrowser/10.1.1503.400'
    }

    def start_requests(self):
        url=self.base_url.format(1)
        yield Request(url=url,cookies=self.cookies,headers=self.headers)
    def parse(self, response):
        total_page = response.xpath('//div[@class="total "]/text()')
        if total_page:
            total_page_num_str = total_page.extract()
            if total_page_num_str:
                allTiticle = re.findall(r'[0-9]\d*', total_page_num_str[0])
                if allTiticle:
                    # for iiii in range(1, int(allTiticle[0])):
                    for iiii in range(1, 5):
                        yield Request(url=self.base_url.format(iiii), callback=self.parse_get_url_per_page,
                                      cookies=self.cookies, headers=self.headers)

    def parse_get_url_per_page(self, response):
        per_company = response.xpath('//div[@class="b-c-white search_result_container"]/div')
        if per_company:
            for iii in per_company:
                company_url = iii.xpath('/a[1]')
                if company_url:
                    per_url = company_url.xpath('@href')
                    yield Request(url=per_url, callback=self.parse_per_company, cookies=self.cookies,
                                  headers=self.headers)

    def parse_per_company(self, response):
        item = CompangItem()
        item['c_id'] = response.url
        name_xpath = response.xpath('//input[@id="_companyName"]/@value').extract()
        if name_xpath:
            item['c_name'] = name_xpath[0]
        c_info_container = response.xpath('//div[@class="company_header_width ie9Style position-rel"]')
        if c_info_container:
            if name_xpath:
                c_name = c_info_container.xpath('div[@class="position-rel"]/h1/text()').extract()
                if c_name:
                    item['c_name'] = c_name
                else:
                    item['c_name'] = response.xpath('/html/head/title/text()').extract()[0].splict('_')[0]
            c_tel = c_info_container.xpath('div[2]/div[2]/div[1]/span[2]/text()')
            if c_tel:
                item['c_tel'] = c_tel.extract()[0]

            c_email = c_info_container.xpath('div[2]/div[2]/div[2]/span[2]/text()')
            if c_email:
                item['c_email'] = c_email.extract[0]

            c_webpage = c_info_container.xpath('div[2]/div[3]/div[1]/span[2]/text()')
            if c_webpage:
                item['c_webpage'] = c_webpage.extract[0]

            c_address = c_info_container.xpath('div[2]/div[3]/div[2]/span[2]/text()')
            if c_address:
                item['c_address'] = c_address.extract[0]

            c_description = c_info_container.xpath('div[2]/div[4]/div[2]/span[2]/text()')
            if c_description:
                item['c_description'] = c_description.extract[0]
        c_gongsi_baseInfo = response.xpath('//div[@id="_container_baseInfo"]')
        if c_gongsi_baseInfo:
            c_leg_people = c_gongsi_baseInfo.xpath('div/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/div/a')
            if c_leg_people:
                item['c_leg_people'] = c_leg_people.extract()[0]
            c_regis_money = c_gongsi_baseInfo.xpath('div/div[2]/table/tbody/tr/td[2]/div[1]/div[2]/div/text')
            if c_regis_money:
                item['c_regis_money'] = c_regis_money.extract()[0]
            c_regis_time = c_gongsi_baseInfo.xpath('div/div[2]/table/tbody/tr/td[2]/div[2]/div[2]/div/text')
            if c_regis_time:
                item['c_regis_time'] = c_regis_time.extract()[0]
            c_regis_address = c_gongsi_baseInfo.xpath('div/div[3]/table/tbody/tr[5]/td[2]')
            if c_regis_address:
                item['c_regis_address'] = c_regis_address.extract()[0]
            c_hangye = c_gongsi_baseInfo.xpath('div/div[3]/table/tbody/tr[3]/td[4]')
            if c_hangye:
                item['c_hangye'] = c_hangye.extract([0])
            c_jingyingfanwei = c_gongsi_baseInfo.xpath('div/div[3]/table/tbody/tr[7]/td[2]/span/span/span[1]/text()')
            if c_jingyingfanwei:
                item['c_jingyingfanwei'] = c_jingyingfanwei
        product_page_total = c_gongsi_baseInfo.xpath('//*[@id="_container_product"]/div/div/div/div/span[1]/text()')
        total_page=0
        if product_page_total:
            total_page_str = re.findall(r'[0-9]\d*', product_page_total.extract()[0])
            if len(total_page_str)!=0:
                total_page=int(total_page_str[0])

        id_xpath = response.xpath('//input[@id="_companyId"]/@value').extract()
        prod_list=[]
        if id_xpath and total_page!=0:
            for iiiii in  range(1,total_page+1):
                prod_url=self.base_product_url.format(iiiii,id_xpath[0])
                html_r=requests.get(prod_url)
                html = html_r.content.decode('utf-8')
                dom_tree = etree.HTML(html)
                prod_list.append(dom_tree.xpath('//body/div/div/table/tbody/tr/td[3]/span/text()').extract())
            item['c_product']=prod_list
        yield item

    # c_regis_num=scrapy.Field()
    # c_regis_area=scrapy.Field()
    # c_regis_money=scrapy.Field()
    # c_leg_people=scrapy.Field()
    # c_company_cat=scrapy.Field()
    # c_regis_status=scrapy.Field()
    # c_regis_jiguan=scrapy.Field()
    # c_regis_address=scrapy.Field()
    # c_hangye=scrapy.Field()
    # c_zhuzhijigou=scrapy.Field()
    # c_regis_time=scrapy.Field()
    # c_product=scrapy.Field()
