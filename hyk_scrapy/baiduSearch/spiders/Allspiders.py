#-*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider,Request
from baiduSearch.items import BaidusearchItem
from scrapy.selector import Selector
from baiduSearch.ContentExtractor import ExtractorToData

text_urls = []
class botspide(CrawlSpider):
    word = ''
    name = "baiduSpiders"
    allowed_domains = []
    start_url = ''
    def __init__(self,word):
        self.word = word
        self.word = self.word.strip()
        self.start_url = "http://www.baidu.com/s?wd=%s" % self.word
    def start_requests(self):
        yield Request(self.start_url,self.baidu_parse)
        
    def baidu_parse(self,response):
        item = BaidusearchItem()
#         self.log(response.body)
        sel = Selector(response)
#         print sel
        for i in range(1,10):
            x_path = '//*[@id="'+str(i)+'"]/h3/a/@href'
            item['new_urls'] = sel.xpath(x_path).extract()
            for new_url in item["new_urls"]:
                yield Request(new_url,self.baidu_parse_1)
        
       
    def baidu_parse_1(self,response):
        item = BaidusearchItem()
        sel = Selector(response)
        item['title1'] = sel.xpath('//@href').extract()
        for aa in item["title1"]:
            if aa.find('.htm') != -1 and aa.find('http:') != -1:
                print aa
                ExtractorToData(aa)
            else:
                try:
                    yield Request(aa,callback=self.baidu_parse_1)
                except:
                    pass

        