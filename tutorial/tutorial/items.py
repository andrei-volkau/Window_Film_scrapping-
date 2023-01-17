# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    id_value = scrapy.Field()
    company_name = scrapy.Field()
    website = scrapy.Field()
    phone = scrapy.Field()
    state = scrapy.Field()
