from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restx import Api
from book_crud.views import api as books_api

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mybookdb',
    'host': 'mongodb',  # Use the service name from Docker Compose
    'port': 27017
}
db = MongoEngine(app)
api = Api(app)
api.add_namespace(books_api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)