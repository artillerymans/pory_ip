# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from pory_ip.Contants.Config import SPIDER_NAME, ALLOWED_DOMAINS, START_URLS
from pory_ip.items import PoryIpItem


class PoryIpSpiderSpider(CrawlSpider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    rules = (
        Rule(LinkExtractor(allow=r'.+www.kuaidaili.com/free/inha/[1-9]/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        trList = response.xpath('//div[@id="list"]/table/tbody/tr')
        for item in trList:
            ip = item.xpath('.//td[1]/text()').get()
            port = item.xpath('.//td[2]/text()').get()
            yield PoryIpItem(ip=ip, port=port)