# spider to crawl all links in article directory starting from the portal page.

import scrapy
import unicodedata
from urllib.parse import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

class PortalSpider(CrawlSpider):
    name = "portal"
    allowed_domains = ["new.wikipedia.org"]
    start_urls = ['https://new.wikipedia.org/wiki/%E0%A4%AE%E0%A5%82_%E0%A4%AA%E0%A5%8C']

    # rules to only follow links in /wiki/ directory
    
    rules = (
        Rule(LinkExtractor(allow=('/wiki/',)), callback='parse_item', follow=True, process_links='filter_links'),
    )
    
    def filter_links(self, links):
        
        # Filter out any link with latin characters [a-zA-Z] in the text
        # This is to avoid crawling pages that are not in the Devanagari script.
        # There are exceptions for robots.txt and the main page. 
        
        for link in links:
            
            # Exceptions for robots.txt and the main page
            if 'robots.txt' in link.url or 'https://new.wikipedia.org/wiki/%E0%A4%AE%E0%A5%82_%E0%A4%AA%E0%A5%8C' in link.url:
                yield link

            # Check if the link text contains any latin characters and filter it out if it does
            if re.search(r'[a-zA-Z]', link.text):
                links.remove(link)
            else:
                yield link



    def parse_item(self, response):
        allowed_section_selector = 'div#mw-content-text.mw-body-content'  # CSS selector for the allowed section

        if (response.css(allowed_section_selector)):
            yield {
                'date': response.css('li#footer-info-lastmod::text').get(),
                'url': response.url,
                'title': response.css('span.mw-page-title-main::text').get(),
                'text': response.css('div.mw-parser-output p::text').getall()[0]
            }
    