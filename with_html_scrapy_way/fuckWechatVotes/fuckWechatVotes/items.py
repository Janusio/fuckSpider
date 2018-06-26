# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FuckwechatvotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WechatVoteArticle(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    abstract = scrapy.Field()
    url = scrapy.Field()


    publish_time = scrapy.Field()
    allText = scrapy.Field()
    to_public_name = scrapy.Field()
    to_public_url = scrapy.Field()
    to_public_num = scrapy.Field()
    to_public_des = scrapy.Field()

    award_des = scrapy.Field()
