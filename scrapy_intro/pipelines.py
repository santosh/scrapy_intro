# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging

# from dotenv import load_dotenv
import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# load_dotenv()

class ScrapyIntroPipeline:
    def __init__(self):
        self.create_mongo_connection()

    def create_mongo_connection(self):
        self.client = pymongo.MongoClient("mongodb://santosh:santosh@localhost:27017/")
        self.db = self.client["quotes"]
        self.collection = self.db["quote"]

        # List all database names
        database_names = self.client.list_database_names()

        # Print the database names
        print("Databases:")
        for db_name in database_names:
            print(f"- {db_name}")
        logging.info("is mongo working?")


    def process_item(self, item, spider):
        # self.store_to_sqlite(item)
        self.store_to_mongo(item)

        print("Quote: " + item['title'])
        return item
    
    def store_to_mongo(self, item):
        self.collection.insert_one(dict(item))

