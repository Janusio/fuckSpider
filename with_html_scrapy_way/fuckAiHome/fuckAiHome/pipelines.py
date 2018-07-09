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
        # item_tel = {'4': '1', '6': '2', '0': '3', '9': '4', '3': '5', '1': '6', '8': '7', '2': '8', '7': '9',
        #          '5': '0'}
        item_tel = {'1': '4', '2': '6', '3': '0', '4': '9', '5': '3', '6': '1', '7': '8', '8': '2', '9': '7','0': '5'}
        try:
            # 插入数据

            if isinstance(item, CompangItem):
                time_str_str = ''
                if item['c_regis_time']:
                    # time_str=item['c_regis_time']
                    # ss=len(item['c_regis_time'])

                    for ii in range(0,len(item['c_regis_time'])):
                        if item['c_regis_time'][ii]!='-':
                            time_str_str+=item_tel[item['c_regis_time'][ii]]
                        else:
                            time_str_str+=item['c_regis_time'][ii]
                    # print(time_str_str)
                self.cursor.execute(
                    """INSERT INTO aihome(c_address, c_description,c_email,c_hangye,c_id,c_leg_people,c_name,c_product,c_regis_address,c_regis_money,c_regis_time,c_tel)
                    VALUE (%s, %s,%s,%s,%s, %s,%s,%s,%s, %s,%s,%s)""",
                    (item['c_address'],
                     item['c_description'],
                     item['c_email'], item['c_hangye'],
                     item['c_id'], item['c_leg_people'],
                     item['c_name'], str(item['c_product']),
                     item['c_regis_address'], item['c_regis_money'],
                     time_str_str, item['c_tel']
                     ))
                self.connect.commit()
                # 4609318275
                # item1 = {'1': '4', '2': '6', '3': '0', '4': '9', '5': '3', '6': '1', '7': '8', '8': '2', '9': '7',
                #         '0': '5'}

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item
