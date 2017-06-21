# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidusearchItem(scrapy.Item):
    new_urls = scrapy.Field()
    title1 = scrapy.Field()
    title2 = scrapy.Field()
    pass
