# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
from pory_ip.Contants.Config import JSON_FILE_NAME, PORT_FILE
import json

class PoryIpPipeline(object):

    def __init__(self):
        self.file = open(JSON_FILE_NAME, 'wb' )
        self.exline = JsonLinesItemExporter(self.file, encoding='utf-8')

    def open_spider(self, spider):
        print("爬虫开始")

    def process_item(self, item, spider):
        self.exline.export_item(item)
        return item

    def close_spider(self, spider):
        print('爬虫结束')
        self.file.close()

        json_file = open(JSON_FILE_NAME, 'r')
        lines = json_file.readlines()
        port_file = open(PORT_FILE, 'w', encoding='utf-8')
        for line in lines:
            map = json.loads(line)
            ip = map.get('ip')
            port = map.get('port')
            port_file.write("http://%s:%s\n"%(ip, port))
        port_file.close()
        json_file.close()
        print('修改端口配置文件完成，可以请爬虫了')