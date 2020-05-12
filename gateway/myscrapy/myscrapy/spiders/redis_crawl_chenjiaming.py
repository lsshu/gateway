# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class RedisCrawlChenjiamingSpider(RedisCrawlSpider):
    name = 'redis_crawl_chenjiaming'
    redis_key = 'redis_crawl_chenjiaming:start_urls'
    allowed_domains = ['chenjiaming.com']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.chenjiaming.com/articlelist\-\d+\-\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'http://www.chenjiaming.com/article-\d+-\d+-\d+.html'), callback='parse_page'),
    )

    def parse_page(self, response):
        item = {}
        item['title'] = response.xpath('//div[@class="allnotice_title"]/h3/text()').extract_first().strip()
        item['url'] = response.url
        return item
