from connect_db import db
from table_models import News

db.drop_tables([News], safe=True)
db.create_tables([News], safe=True)
