# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WikiscraperPipeline:
    def process_item(self, item, spider):
        return item

# Check if date item is empty
# Remove a "Last edited on " and everything after "," from the text of each date item
class DatePipeline:
    def process_item(self, item, spider):
        # Check if date item is empty or empty string
        if item['date'] == None or item['date'] == '':
            item['date'] = 'No date found'
        else: 
            # Remove everything after "," from the text of each date item
            item['date'] = item['date'].split(',')[0]
            # Remove "Last edited on " from the text of each date item
            item['date'] = item['date'].split(' ')[-3:]
            
        return item

