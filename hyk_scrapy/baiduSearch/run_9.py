# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
def run_spider(inword):
    para_list = ['scrapy', 'crawl','baiduSpiders','-a']
    input_word = 'word='+inword
    para_list.append(input_word)
#     print para_list
    execute(para_list)

# run_spider("劳动法")