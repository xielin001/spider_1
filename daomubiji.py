# -*- coding: utf-8 -*-
import scrapy


class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://daomubiji.com/']

    def parse(self, response):
        pass
