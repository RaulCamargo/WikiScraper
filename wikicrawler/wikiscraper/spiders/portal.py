# spider to pull links from portal page (https://new.wikipedia.org/wiki/%E0%A4%AE%E0%A5%82_%E0%A4%AA%E0%A5%8C) and saves them to a file.

import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import PortalItem

class PortalSpider(CrawlSpider):
    name = 'portal'

    # restricts the crawl to pages within the new.wikipedia.org domain
    allowed_domains = ['new.wikipedia.org']
    start_urls = ['https://new.wikipedia.org/wiki/%E0%A4%AE%E0%A5%82_%E0%A4%AA%E0%A5%8C']

    # uses a LinkExtractor to find links to other pages within the same domain 
    rules = [Rule(LinkExtractor(allow='https://new.wikipedia.org/wiki/'), callback='parse_info', follow=False)]

    # parses the response, ignores page if it has already been visited,
    # ignores page with 
    # and saves url to json file
    def parse_info(self, response):
        item = PortalItem()
        item['url'] = response.url
        yield item

# Run this spider with the following command:
# scrapy crawl portal -o links.csv:csv

    

