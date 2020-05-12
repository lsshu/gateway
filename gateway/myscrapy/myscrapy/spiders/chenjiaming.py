# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myscrapy.items import MyscrapyItem


class ChenjiamingSpider(CrawlSpider):
    name = 'chenjiaming'
    allowed_domains = ['www.chenjiaming.com']
    start_urls = ['http://www.chenjiaming.com/articlelist-12-1.html']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.chenjiaming.com/articlelist\-\d+\-\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'http://www.chenjiaming.com/article-\d+-\d+-\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MyscrapyItem()
        item['title'] = response.xpath('//div[@class="allnotice_title"]/h3/text()').extract_first().strip()
        item['user'] = 1
        # item['url'] = response.url
        return item
