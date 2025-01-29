import scrapy

from ..items import MiniPC

class MinipcSpider(scrapy.Spider):
    name = "minipc"
    start_urls = ["https://www.amazon.com/s?k=dell+optiplex"]

    def parse(self, response):
        minipc = MiniPC()
        search_results = response.css("div[role='listitem']")

        for result in search_results:
            title_recipe = result.css('div[data-cy="title-recipe"]')
            title = title_recipe.css("h2 span::text").get()

            relative_url = title_recipe.css("a.a-link-normal::attr(href)").get()
            price = result.css(".a-price .a-offscreen::text").get()
            rating = result.css("i[data-cy='reviews-ratings-slot'] span::text").get()

            minipc["title"] = title
            minipc["price"] = price
            minipc["url"] = relative_url
            minipc["rating"] = rating

            yield minipc


