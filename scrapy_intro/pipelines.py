# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class ScrapyIntroPipeline:
    def __init__(self):
        self.create_mongo_connection()

    def create_mongo_connection(self):
        self.client = pymongo.MongoClient("mongodb://santosh:santosh@localhost:27017/")
        self.db = self.client["amazon"]
        self.collection = self.db["minipc"]

    def process_item(self, item, spider):
        self.store_to_mongo(item)
        return item
    
    def store_to_mongo(self, item):
        self.collection.insert_one(dict(item))
