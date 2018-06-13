# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScbusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    busId=scrapy.Field()
    busName = scrapy.Field()
    busUrl = scrapy.Field()
    busTime = scrapy.Field()
    busPrice = scrapy.Field()
    busCompany = scrapy.Field()
    busUpdateTime = scrapy.Field()
    busType = scrapy.Field()
    busImage = scrapy.Field()
    cityUrl=scrapy.Field()
    cityName=scrapy.Field()

class StationItem(scrapy.Item):
    stationId=scrapy.Field()
    stationName=scrapy.Field()
    stationSorted=scrapy.Field()
    stationUrl=scrapy.Field()
    busUrl=scrapy.Field()

class CityItem(scrapy.Item):
    cityId=scrapy.Field()
    cityName=scrapy.Field()
    cityPinyin=scrapy.Field()
    cityUrl=scrapy.Field()
    cityProvince=scrapy.Field()
class cityNumberFront(scrapy.Item):
    listId=scrapy.Field()
    listName=scrapy.Field()
    listUrl=scrapy.Field()
    cityUrl=scrapy.Field()