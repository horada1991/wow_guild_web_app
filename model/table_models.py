from peewee import *
from connect_db import db


class BaseModel(Model):
    class Meta:
        database = db


class News(BaseModel):
    title = CharField()
    body = CharField()
    timestamp = TimestampField()

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'timestamp': self.timestamp
        }
