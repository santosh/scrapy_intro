import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from ..items import QuoteItem

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ["https://quotes.toscrape.com/login"]

    def __init__(self):
        self.download_delay = 3

    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'admin',
            'password': 'admin'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        items = QuoteItem()

        all_div_quotes = response.css("div.quote")

        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").extract_first()
            author = quotes.css(".author::text").extract_first()
            tag = quotes.css(".tag::text").extract()

            items["title"] = title
            items["author"] = author
            items["tag"] = tag

            yield items

        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

