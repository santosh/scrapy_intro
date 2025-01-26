# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyIntroPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""create table if not exists quote(
            title text,
            author text,
            tag text)""")

    def process_item(self, item, spider):
        self.store_to_db(item)
        print("Quote: " + item['title'])
        return item

    def store_to_db(self, item):
        self.curr.execute("""insert into quote values (?,?,?)""", (
            item['title'],
            item['author'],
            ",".join(item['tag'])
        ))

        self.conn.commit()
