import scrapy


class MinipcSpider(scrapy.Spider):
    name = "minipc"
    allowed_domains = ["amazon.in"]
    start_urls = ["https://amazon.in"]

    def parse(self, response):
        pass
