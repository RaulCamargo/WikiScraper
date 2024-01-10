# spider to crawl all links in article directory starting from the portal page.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PortalSpider(CrawlSpider):
    name = "portal"
    allowed_domains = ["new.wikipedia.org"]
    start_urls = ['https://new.wikipedia.org/wiki/%E0%A4%AE%E0%A5%82_%E0%A4%AA%E0%A5%8C']

    # rules to only follow links in /wiki/ directory
    
    rules = (
        Rule(LinkExtractor(allow=('/wiki/',)), process_links='filter_links', callback='parse_item', follow=True),
    )
    
    def filter_links(self, links):
        # This method allows only links within the specified section.
        # Adjust the selectors based on your HTML structure.

        # allowed_links = []

        # allowed_section_selector = 'div#mw-content-text.mw-body-content'  # CSS selector for the allowed section

        # for link in links:
        #     if link.url.startswith(tuple(self.start_urls)) or link.url.endswith('robots.txt') or (
        #             response and response.css(allowed_section_selector)):
        #         allowed_links.append(link)

        return links


    def parse_item(self, response):
        allowed_section_selector = 'div#mw-content-text.mw-body-content'  # CSS selector for the allowed section

        if (
            response.url.startswith(tuple(self.start_urls)) or
            response.url.endswith('robots.txt') or
            response.css(allowed_section_selector)
        ):
            yield {
                'date': response.css('li#footer-info-lastmod::text').get(),
                'url': response.url,
                'title': response.css('span.mw-page-title-main::text').get(),
                'text': response.css('div.mw-parser-output p::text').getall()[0]
            }
    
    # # print response.title to console
    # def parse(self, response):
    #     print(response.title)

    
    

