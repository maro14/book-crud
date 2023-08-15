from flask import request, jsonify
from app.app import app
from app.models import Book

@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        books = Book.objects.all()
        return jsonify([{"id": str(book.id), "title": book.title, "author": book.author} for book in books])
    elif request.method == 'POST':
        data = request.get_json()
        book = Book(**data).save()
        return jsonify({"id": str(book.id), "title": book.title, "author": book.author}), 201

@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    book = Book.objects.get_or_404(id=book_id)
    if request.method == 'GET':
        return jsonify({"id": str(book.id), "title": book.title, "author": book.author})
    elif request.method == 'PUT':
        data = request.get_json()
        book.update(**data)
        return jsonify({"id": str(book.id), "title": book.title, "author": book.author})
    elif request.method == 'DELETE':
        book.delete()
        return '', 204
