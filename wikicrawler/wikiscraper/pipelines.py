# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WikiscraperPipeline:
    def process_item(self, item, spider):
        return item

# Remove a "Last edited on " and everything after "," from the text of each date item
# class DatePipeline:
#     def process_item(self, item, spider):
#         item['date'] = item['date'].split(',')[0].split('Last edited on ')[1]
#         return item
    
    