# Define here the consumers for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FooItem(scrapy.Item):
    index = scrapy.Field()
    url = scrapy.Field()
    live = scrapy.Field()
    job_description = scrapy.Field()
