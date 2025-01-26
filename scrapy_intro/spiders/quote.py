import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        all_div_quotes = response.css("div.quote")
        title = all_div_quotes.css("span.text::text").extract()
        author = all_div_quotes.css(".author::text").extract()
        tag = all_div_quotes.css(".tag::text").extract()
        yield {'title': title, 'author': author, 'tag': tag}
