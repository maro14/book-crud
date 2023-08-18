from book_crud import db

class Book(db.Document):
    title = db.StringField(required=True, max_length=100)
    author = db.StringField(required=True, max_length=50)
