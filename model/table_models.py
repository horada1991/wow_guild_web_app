from peewee import *
from connect_db import db


class BaseModel(Model):
    class Meta:
        database = db

    # convert peewee object into a dictionary with attribute, value pairs
    def convert_object_to_dict(self):
        return dict((attr, value) for attr, value in vars(self)['_data'].items())


# model for news table to store news on the main page
class News(BaseModel):
    title = CharField()
    body = CharField()
    timestamp = TimestampField()
