from table_models import *


# Template for handle sql tables
class TableHandler:
    def get_all_entry(self):
        return [entry for entry in self.table.select()]

    def save_entry(self, entry_dictionary):
        self.table.create(**entry_dictionary)


# this class handles the news table ind the database
class NewsHandler(TableHandler):
    def __init__(self):
        self.table = News
