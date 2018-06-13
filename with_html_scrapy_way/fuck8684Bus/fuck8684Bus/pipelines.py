# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from logging import log

import pymysql
import json
import codecs
from with_html_scrapy_way.fuck8684Bus.fuck8684Bus import settings
from with_html_scrapy_way.fuck8684Bus.fuck8684Bus.items import *


class ScbusPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = codecs.open('items.jl', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"

        # print(line)
        # self.file.write(line.encode("utf-8"))
        return item


class DBPipeline(object):
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
            if isinstance(item, StationItem):
                self.cursor.execute(
                    """INSERT INTO roadRun(stationName, stationUrl,busUrl,stationSorted)
                    VALUE (%s, %s,%s,%s)""",
                    (item['stationName'],
                     item['stationUrl'],
                     item['busUrl'],
                     item['stationSorted']
                     ))
                self.connect.commit()
            elif isinstance(item, ScbusItem):
                self.cursor.execute(
                    """INSERT INTO busesefwithcity(busName, busUrl,busTime,busPrice,busCompany,busUpdateTime,busType,busImage,cityName)
                    VALUE (%s, %s, %s, %s,%s,%s,%s, %s,%s)""",
                    (item['busName'],
                     item['busUrl'],
                     item['busTime'],
                     item['busPrice'],
                     item['busCompany'],
                     item['busUpdateTime'],
                     item['busType'],
                     item['busImage'],
                     item['cityName']
                     ))
            elif isinstance(item, CityItem):
                self.cursor.execute(
                    """INSERT INTO cityesef(cityName, cityPinyin,cityUrl,cityProvince)
                    VALUE (%s, %s, %s, %s)""",
                    (item['cityName'],
                     item['cityPinyin'],
                     item['cityUrl'],
                     item['cityProvince']
                     ))
        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item
