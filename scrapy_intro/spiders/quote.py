import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # in this example, extract <title> of the page
        title = response.css('title::text').extract()
        yield {'titletext': title}

        # extract all quotes
        quotes = response.css('div.quote>span.text::text').extract()

        yield {'quotes': quotes}

        # extract all authors
        authors = response.css('div.quote>span small.author::text').extract()
        yield {'authors': authors}
