from flask import request, jsonify
from flask_restx import Namespace, fields, Resource
from mongoengine.errors import DoesNotExist, ValidationError
from book_crud.models import Book

api = Namespace('books', description='Book operation')

book_model = api.model('Book', {
    'id': fields.String(required=True, description='Book ID'),
    'title': fields.String(required=True, description='Book title'),
    'author': fields.String(required=True, description='Book author')
})

@api.route('/books')
class BookList(Resource):
    @api.marshal_list_with(book_model)
    def get(self):
        try:
            books = Book.objects.all()
            return books
        except Exception as e:
            api.abort(500, message='Internal server error')
            
    @api.expect(book_model)
    @api.marshal_with(book_model, code=201)
    def post(self):
        try:
            data = api.payload
            book = Book(**data).save()
            return book, 201
        except ValidationError as ve:
            api.abort(400, message=ve.message)
        except Exception as e:
            api.abort(500, message='Internal server error')