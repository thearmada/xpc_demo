# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request

class DiscoverySpider(scrapy.Spider):
    name = 'discovery'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/sort-like']

    def parse(self, response):
        url = 'http://www.xinpianchang.com/%s?from=ArticleList'
        posts = response.xpath('//ul[@class="video-list"]/li')
        for post in posts:
            pid = post.xpath('./@data-articleid').extract_first()
            request = Request(url % pid, callback=self.parse_post)
            request.meta['pid'] = pid
            request.meta['thumbnail'] = post.xpath('./a/img/@_src').get()
            print(request.meta)
            #yield request

    def parse_post(self, response):
        pass
