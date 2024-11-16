import scrapy


class ScrapingSpiderSpider(scrapy.Spider):
    name = "scraping_spider"
    allowed_domains = ["sample.com"]
    start_urls = ["https://sample.com"]

    def parse(self, response):
        pass
