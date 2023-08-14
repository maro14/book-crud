from app import db
from datetime import datetime


class Book(db.Document):
    title = db.StringField(required=True)
    author = db.StringField(required=True)
    year = db.IntField()
    timestamp = db.DateTimeField(default=datetime.utcnow)
