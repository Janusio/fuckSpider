# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FucksoufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SoufangCityAllWithProvinceItem(scrapy.Item):
    provinceName = scrapy.Field()
    provinceId = scrapy.Field()


class SoufangCityAllWithCityItem(scrapy.Item):
    cityName = scrapy.Field()
    cityUrl = scrapy.Field()
    provinceId = scrapy.Field()


class SoufangCityAllWithAreaItem(scrapy.Item):
    areaName = scrapy.Field()
    areaUrl = scrapy.Field()
    cityId = scrapy.Field()
