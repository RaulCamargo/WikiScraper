# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# Class that extends scrapy.Item. Will be used to store the date, title, text, and URL of the article.
class ArticleItem(scrapy.Item):
    date = scrapy.Field()
#     title = scrapy.Field()
#     text = scrapy.Field()
#     url = scrapy.Field()