# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class AdcspiderPipeline:
    def __init__(self):
        host = 'localhost'
        user = 'root'
        passwd = 'root'
        port = 3306
        db = 'yglz'
        charset = 'utf8'
        self.db = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset,
            port=port)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO tousu(type,time,title) VALUES(%s,%s,%s) '
        self.cur.execute(sql, (item['newsType'], item['newsTime'], item['newsTitle']))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
