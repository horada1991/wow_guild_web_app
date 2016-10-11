from table_models import *


# Template for handle sql tables
class TableHandler:
    def __init__(self, table):
        self.table = table

    def get_all_entry(self):
        return [entry for entry in self.table.select()]

    def save_entry(self):
        raise NotImplementedError


# this class handles the news table ind the database
class NewsHandler(TableHandler):
    def __init__(self):
        super().__init__(News)

    def save_entry(self, entry_dictionary):
        import datetime
        import time
        now = datetime.datetime.now()
        self.table.create(**entry_dictionary, timestamp=time.mktime(now.timetuple()))
