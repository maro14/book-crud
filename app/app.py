from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'library',
    'host': 'db',
    'port': 27017
}

db = MongoEngine(app)

@app.route('/')
def index():
    return "Hello"

if __name__ == "__main__":
    app.run()