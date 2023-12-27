# Filters out any url with latin script after teh /wiki/ part of the url
# This is to avoid scraping pages that are not in the target language

import re
from scrapy.downloadermiddlewares.httpcompression import HttpCompressionMiddleware

class LatinFilterMiddleware(HttpCompressionMiddleware):
    def process_request(self, request, spider):
        path = request.url.split('/', 4)[-1]
        if re.search(r'[a-zA-Z]', path):
            spider.logger.info('Dropping request due to Latin characters: {}'.format(request.url))
            return None
        else:
            return super().process_request(request, spider)
    