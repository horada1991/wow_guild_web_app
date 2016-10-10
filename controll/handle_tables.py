from table_models import *


class TableHandler:
    def __init__(self, table):
        self.table=table

    def get_all_entry(self):
        return self.table.select()

    def save_entry(self, entry_dictionary):
        self.table.create(**entry_dictionary)
