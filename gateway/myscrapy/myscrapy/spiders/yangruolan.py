# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class YangruolanSpider(CrawlSpider):
    name = 'yangruolan'
    allowed_domains = ['www.yangruolan.com']
    start_urls = ['https://www.yangruolan.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.yangruolan.com/mood/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        post_box = response.xpath('//div[@class="post_box"]')

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
