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

        # another example using xpath
        for quote in response.xpath('//div[@class="quote"]'):
            text = quote.xpath('span[@class="text"]/text()').extract_first()
            author = quote.xpath('span/small[@class="author"]/text()').extract_first()
            yield {'text': text, 'author': author}

        # combining css selectors and xpath
        next_link = response.css("li.next a").xpath("@href").extract_first()
        
        yield {'next_link': next_link}
