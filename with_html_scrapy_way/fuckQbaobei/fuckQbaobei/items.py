# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FuckqbaobeiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class GushiDetailItem(scrapy.Item):
    title=scrapy.Field()
    gushi_detail=scrapy.Field()
    gushi_comment=scrapy.Field()

