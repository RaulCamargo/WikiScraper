# spider to crawl all links in article directory starting from the portal page.

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiscraper.items import ArticleItem

# Create a new spider class called PortalSpider that extends CrawlSpider.
class PortalSpider(CrawlSpider):
    name = 'portal'
    # Restrict the spider to only crawl links from the new.wikipedia.org
    allowed_domains = ['new.wikipedia.org']
    
    # Start the spider from the portal page.
    start_urls = ['https://new.wikipedia.org/wiki/%E0%A4%AE%E0%A5%82_%E0%A4%AA%E0%A5%8C']

    # Spider searches links in the /wiki/ subdirectory and calls parse_item() for each link.
    rules = (
        Rule(LinkExtractor(allow=r'/wiki/'), callback='parse_item', follow=True),
    )

    # Parse the article page
    def parse_item(self, response):
        item = ArticleItem()
        
        # Extract the date for the last update of the article.
        date = item.add_xpath('//div[@class="mw-footer-container"]//li[@id="footer-info-lastmod"]/text()').get()
