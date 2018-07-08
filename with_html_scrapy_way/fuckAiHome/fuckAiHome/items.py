# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FuckaihomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CompangItem(scrapy.Item):
    c_id=scrapy.Field()
    c_tel=scrapy.Field()
    c_name=scrapy.Field()
    c_email=scrapy.Field()
    c_webpage=scrapy.Field()
    c_address=scrapy.Field()
    c_description=scrapy.Field()
    c_regis_num=scrapy.Field()
    c_regis_area=scrapy.Field()
    c_regis_money=scrapy.Field()
    c_leg_people=scrapy.Field()
    c_company_cat=scrapy.Field()
    c_regis_status=scrapy.Field()
    c_regis_jiguan=scrapy.Field()
    c_regis_address=scrapy.Field()
    c_hangye=scrapy.Field()
    c_jingyingfanwei=scrapy.Field()
    c_regis_time=scrapy.Field()
    c_product=scrapy.Field()
