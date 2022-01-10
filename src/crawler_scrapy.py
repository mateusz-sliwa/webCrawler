from scrapy.spiders import Spider
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

class stackOvelflowSpider(Spider):
    name = 'stackoverflow'
    allowed_domains = ['www.stackoverflow.com']
    start_urls = ["https://www.stackoverflow.com"]

    def parse(self, response):
        pass
    
class stackOverflowCrawler(CrawlSpider):
    name = 'stackoverflow'
    allowed_domains = ['www.stackoverflow.com']
    start_urls = ["https://stackoverflow.com"]
    rules = (Rule(LinkExtractor()),)