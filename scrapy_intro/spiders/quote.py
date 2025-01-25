import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # in this example, extract <title> of the page
        title = response.css('title::text').extract()
        yield {'titletext': title}
