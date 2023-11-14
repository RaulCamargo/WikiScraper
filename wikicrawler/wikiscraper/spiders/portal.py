# spider to crawl all links in article directory starting from the portal page.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PortalSpider(CrawlSpider):
    name = "portal"
    allowed_domains = ["new.wikipedia.org"]
    start_urls = ['https://new.wikipedia.org/wiki/%E0%A4%AE%E0%A5%82_%E0%A4%AA%E0%A5%8C']

    # rules to only follow links in /wiki/ directory
    # and ignore URLs with latin script
    rules = (
        Rule(LinkExtractor(allow=('/wiki/'), deny=('RecentChanges', 'Search', 'MyContributions', 'MyTalk', 'WhatLinksHere', 'SpecialPages', 'BAnand', 'Statistics')), callback='parse_item', follow=True),
    )
    
    # parse the page and save the date last modified,
    # save the url,
    # save the title,
    # save text from the first <p> tag in <div class="mw-parser-output"> if it contains more than 3 "|" characters
    def parse_item(self, response):
        if response.css('div.mw-parser-output p::text').getall():
            if response.css('div.mw-parser-output p::text').getall()[0].count('|') > 3:
                yield {
                    'date': response.css('li#footer-info-lastmod::text').get(),
                    'url': response.url,
                    'title': response.css('h1#firstHeading::text').get(),
                    'text': response.css('div.mw-parser-output p::text').getall()[0]
                }
    
    # print response.title to console
    def parse(self, response):
        print(response.title)

    