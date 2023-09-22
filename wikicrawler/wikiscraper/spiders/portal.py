# spider to crawl all links in article directory starting from the portal page.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PortalSpider(CrawlSpider):
    name = "portal"
    allowed_domains = ["https://new.wikipedia.org/"]
    start_urls = ['https://new.wikipedia.org/w/index.php?title=विशेष:AllPages&from="अपूर्व+चकोतरर्कळ्+(तमिल+संकिपा)']
    