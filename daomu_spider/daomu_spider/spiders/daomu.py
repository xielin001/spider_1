# -*- coding: utf-8 -*-
import urllib
import bs4
import scrapy
from scrapy.selector import XPathSelector


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com/zang-hai-hua']
    start_urls = ['http://daomubiji.com/zang-hai-hua/']
    # for url in start_urls:
    #     html = urllib.request.urlopen(url).read()
    #     soup = bs4.BeautifulSoup(html)
    #     response = soup.select('article > a')
    # print(response)
    def parse(self, response):
        selector = XPathSelector(response)
        print('爬取源码完毕。。。')

