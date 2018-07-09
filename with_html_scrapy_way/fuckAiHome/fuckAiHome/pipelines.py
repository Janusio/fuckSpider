# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from with_html_scrapy_way.fuckAiHome.fuckAiHome.items import *
from with_html_scrapy_way.fuckAiHome.fuckAiHome import settings
import pymysql
import json
import codecs


class FuckaihomePipeline(object):
    def process_item(self, item, spider):
        return item


class FuckaihomeDbPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            # 插入数据
            if isinstance(item, FuckaihomeItem):
                time_str=item['c_regis_time']

                for ii in item['c_regis_time']:
                    time_str.replace(ii,)

                self.cursor.execute(
                    """INSERT INTO aihome(c_address, c_description,c_email,c_hangye,c_id,c_leg_people,c_name,c_product,c_regis_address,c_regis_money,c_regis_time,c_tel)
                    VALUE (%s, %s,%s,%s)""",
                    (item['c_address'],
                     item['c_description'],
                     item['c_email'], item['c_hangye'],
                     item['c_id'], item['c_leg_people'],
                     item['c_name'], item['c_product'],
                     item['c_regis_address'], item['c_regis_money'],
                     item['c_regis_time'], item['c_tel']
                     ))
                self.connect.commit()
                # 4609318275
                item1 = {'1': '4', '2': '6', '3': '0', '4': '9', '5': '3', '6': '1', '7': '8', '8': '2', '9': '7',
                        '0': '5'}

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item
