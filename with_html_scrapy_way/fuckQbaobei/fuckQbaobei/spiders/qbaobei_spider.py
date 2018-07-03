import scrapy
from scrapy.http import HtmlResponse, Request
from with_html_scrapy_way.fuckQbaobei.fuckQbaobei.items import *
import re


class QBaobeiSpider(scrapy.Spider):
    name = "qBaoBeiSpider"
    allowed_domains = ["qbaobei.com"]
    base_url = 'http://www.qbaobei.com/jiaoyu/yegs/sqgs/'
    base_url_with_page = 'http://www.qbaobei.com/jiaoyu/yegs/sqgs/List_{}.html'
    start_urls = ['http://www.qbaobei.com/jiaoyu/yegs/sqgs/']

    def parse(self, response):
        all_page = response.xpath('//div[@class="page"]/a[@class="end"]/text()').extract()[0]
        allTiticle = re.findall(r'[0-9]\d*', all_page)
        allNum = ''
        for ii in allTiticle:
            allNum += ii
        for i in range(1, int(allNum)):
            yield Request(url=self.base_url_with_page.format(i), callback=self.parse_per_list_page)

    def parse_per_list_page(self, response):
        per_page_list = response.xpath('//div[@class="news-list-main"]//ul//li')
        for iii in per_page_list:
            per_gushi_url = iii.xpath('a/@href').extract()[0]
            yield Request(url=per_gushi_url, callback=self.per_gushi_detail)

    def per_gushi_detail(self, response):
        item = GushiDetailItem()
        item["title"] = response.xpath('//div[@class="detail-list"]//div[@class="news-title"]//h1/text()').extract()[0]
        gushi_info = response.xpath('//div[@class="detail-box"]')
        txtAbstractClear = ''
        for iii in gushi_info:
            per_title=None
            if iii.xpath('h2/text()'):
                per_title=iii.xpath('h2/text()').extract()[0]
                txtAbstractClear += ('[' + iii.xpath('h2/text()').extract()[0] + ']')
                txtAbstractClear+='\n'
            str_info = iii.extract()
            str_no_kuohao=re.sub(r'<.*?>', "", str_info)
            if per_title:
                str_no_kuohao=str_no_kuohao.replace(per_title,"",1)
            txtAbstractClear += re.sub(r'[\n \r\t\xa0]', "", str_no_kuohao)
            txtAbstractClear += '\n'
        item["gushi_detail"] = txtAbstractClear
        yield item
