import re
import scrapy
import string
from urlparse import urljoin
from demo.items import DemoItem
from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from sets import Set

def info(msg):
    log.msg(str(msg), level=log.INFO)

class CnnSpider(CrawlSpider):
    name = "cnn"
    allowed_domains = ["cnn.com"]
    start_urls = [
        "http://edition.cnn.com/",
    ]
    keywords = [u'sport', u'world', u'tech', u'entertainment', u'travel']
#    keywords = ['sport']
    count = 1;
    urlSet = Set(start_urls)

    rules = (
         Rule(sle(allow=(r"/2015/05/??", )), callback="parse_1", follow=True
              , process_request='_process_request'),
         )
    def parse_1(self, response):
        items = []
        url = response.url
        for sel in response.xpath('//head'):
            item = DemoItem()
            
            item['title'] = sel.xpath('./meta[contains(@property,"title")]/@content').extract()
            selkeywords = sel.xpath('./meta[contains(@name,"keywords")]/@content').extract()
            item['desc'] = sel.xpath('./meta[contains(@property,"description")]/@content').extract()
            item['link'] = sel.xpath('./meta[contains(@property,"url")]/@content').extract()
            item['image_urls'] = sel.xpath('./meta[contains(@property,"image")]/@content').extract()
            if item['title']==[] or selkeywords==[] or item['desc'] == [] or item['link'] == [] or item['image_urls'] == []:
                continue
        
            exist = False
            words = []
            for key in self.keywords:
                if string.find(selkeywords[0], key)>-1:
                    exist = True
                    words.append(key)
            if not exist:
                continue
            item['keywords']=words
            print item['keywords'][0]
#            item['type'] = sel.xpath('./meta[contains(@property,"type")]/@content').extract()
            item['pubdate'] = sel.xpath('./meta[contains(@property,"pubdate")]/@content').extract()
#            item['site_name'] = sel.xpath('./meta[contains(@property,"site_name")]/@content').extract()
            item['author'] = sel.xpath('./meta[contains(@name,"author")]/@content').extract()
            item['id'] = str(self.count)
            self.count = self.count+1
            items.append(item)
        return items
            
    def _process_request(self, request):
        if str(request) in self.urlSet:
            return None
#        if self.count>100:
#            return None

        self.urlSet.add(str(request))
#        print str(request)
        return request


