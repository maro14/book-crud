from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mybookdb',
    'host': 'mongodb',  # Use the service name from Docker Compose
    'port': 27017
}
db = MongoEngine(app)

from app import views
