from peewee import *
from connect_db import db


class BaseModel(Model):
    class Meta:
        database = db

    def convert_object_to_dict(self):
        return dict((attr, value) for attr, value in vars(self)['_data'].items())


class News(BaseModel):
    title = CharField()
    body = CharField()
    timestamp = TimestampField()
