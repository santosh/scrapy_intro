# Scrapy Kickstart

Learning Scrapy through doing it.

## About the project

- Run quote crawler:

    scrapy crawl quote


This runs crawler or spider defined in file `spiders/quote.py`. Other spiders can be run the same way. 

- Use "Item" containers to store fetched data before putting into any kind of pipeline. See `items.py` for the schema.
- These items are then accessed in the pipeline. See `pipelines.py`. Pipelines can be used to store scraped data to the database among other things.
