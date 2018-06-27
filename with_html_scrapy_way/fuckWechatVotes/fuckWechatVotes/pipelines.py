# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import json
import codecs

from fuckWechatVotes import settings
from fuckWechatVotes.items import *


class FuckwechatvotesPipeline(object):
    def process_item(self, item, spider):
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
            if isinstance(item, WechatVoteArticle):
                self.cursor.execute(
                    """INSERT INTO voteforkey(title, abstract,allText,award_des,publish_time,to_public_des,to_public_name,to_public_num,url)
                    VALUE (%s, %s,%s,%s,%s,%s, %s,%s,%s)""",
                    (item['title'],
                     item['abstract'],
                     item['allText'],
                     item['award_des'],
                     item['publish_time'],
                     item['to_public_des'],
                     item['to_public_name'],
                     item['to_public_num'],
                     item['url']
                     ))
                self.connect.commit()
        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item
