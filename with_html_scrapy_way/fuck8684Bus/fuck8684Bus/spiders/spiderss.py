import sys
from importlib import reload

reload(sys)
import json
from scrapy.http import HtmlResponse, Request
from with_html_scrapy_way.fuck8684Bus.fuck8684Bus.items import *


class Bus8684(scrapy.Spider):
    name = "bus8684"
    allowed_domains = ["8684.cn"]
    start_urls = []

    def start_requests(self):
        file_object = open('numberlist.txt', 'r')
        try:
            url_head = "http://chengdu.8684.cn/"
            for line in file_object:
                self.start_urls.append(url_head + line.replace("\n", ""))
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            file_object.close()

    def parse(self, response):
        filename = response.url.split("/")[-1]
        # with open(filename,'wb') as  f:
        #     f.write(response.body)
        for sel in response.xpath('/html/body/div[6]/div[1]/div[2]/div[2]/a'):
            # print(sel)
            item = ScbusItem()
            item['busName'] = sel.xpath('text()').extract()
            item['busUrl'] = sel.xpath('@href').extract()
            yield item


class Station8684(scrapy.Spider):
    name = "station8684"
    # 不能写chengdu.8684.cn
    allowed_domains = ["8684.cn"]
    start_urls = ["http://js.8684.cn/citys/city_boxInf.min.js"]
    url_head = "http://{city_name}.8684.cn{url}"

    # def start_requests(self):
    #     file_object=open('numberlist.txt','r')
    #     try:
    #         for line in file_object:
    #             self.start_urls.append(self.url_head+line.replace("\n",""))
    #         for url in self.start_urls:
    #             yield self.make_requests_from_url(url)
    #     finally:
    #         file_object.close()
    def parse(self, response):
        # print(bytes.decode(response.body).replace('{','["').replace('var','{').replace('=',":").replace('{','{"').replace(':','":').replace(',',',"').replace('}',']')+'}')
        ll = response.body.decode('utf-8').split('citysfjson=')[-1].replace(';', '').replace('{', '{"').replace(':"',
                                                                                                                '":"').replace(
            ',', ',"').replace('""', '"')
        json_data2 = json.loads(ll)
        for (key, value) in json_data2.items():
            for (key1, value1) in value.items():
                item0 = CityItem()
                item0['cityProvince'] = key
                item0['cityUrl'] = self.url_head.format(city_name=key1, url='')
                item0['cityName'] = value1
                item0['cityPinyin'] = key1
                yield item0
                yield Request(url=item0['cityUrl'],
                              meta={'cityName': item0['cityPinyin']},
                              callback=self.parse_per_bus_num_list)

    def parse_per_bus_num_list(self, response):
        item4 = cityNumberFront()
        url = response.url
        for sel in response.xpath('/html/body/div[7]/div[1]/div[2]/div[1]/a'):
            item4['listUrl'] = url + sel.xpath('@href').extract()[0]
            cityName = response.meta['cityName']
            yield item4
            yield Request(url=item4['listUrl'],
                          meta={'cityName': cityName},
                          callback=self.parse_bus)

    def parse_bus(self, response):
        # filename = response.url.split("/")[-1]
        # with open(filename,'wb') as  f:
        #     f.write(response.body)
        cityName = response.meta['cityName']
        for sel in response.xpath('/html/body/div[6]/div[1]/div[2]/div[2]/a'):
            # print(sel)
            item = ScbusItem()
            item['busName'] = sel.xpath('text()').extract()
            item['busUrl'] = sel.xpath('@href').extract()
            for perItem in item:
                urlll=self.url_head.format(city_name=cityName, url=item['busUrl'][0])
                yield Request(url=self.url_head.format(city_name=cityName, url=item['busUrl'][0]),
                              meta={'url_per': item['busUrl'], 'bus_name': item['busName'],'cityName': cityName},
                              callback=self.parse_per_bus)

    def parse_per_bus(self, response):
        # filename=response.url.split("/")[-1]
        # with open(filename,'wb') as  f:
        #     f.write(response.body)
        cityName = response.meta['cityName']
        for sel in response.xpath('/html/body/div[6]/div[1]/div[2]/div[1]'):
            item1 = ScbusItem()
            item1['busImage'] = sel.xpath('img/@src').extract()
            item1['busType'] = sel.xpath('div[1]/div[1]/a/text()').extract()
            item1['busTime'] = sel.xpath('div[1]/p[1]/text()').extract()
            item1['busPrice'] = sel.xpath('div[1]/p[2]/text()').extract()
            item1['busCompany'] = sel.xpath('div[1]/p[3]/a/text()').extract()
            item1['busUpdateTime'] = sel.xpath('div[1]/p[4]/text()').extract()
            item1['busUrl'] = response.meta['url_per']
            item1['busName'] = response.meta['bus_name']
            item1['cityName']=response.meta['cityName']
            yield item1

        for sel in response.xpath('/html/body/div[6]/div[1]/div[2]/div[@class="bus_line_site "]/div[1]/div'):
            # print(sel)
            # print('ssssssssssssssssssssssssss')
            item2 = StationItem()
            item2['stationName'] = sel.xpath('a/text()').extract()
            item2['stationUrl'] = sel.xpath('a/@href').extract()
            item2['stationSorted'] = sel.xpath('i/text()').extract()
            item2['busUrl'] = response.meta['url_per']
            yield item2
