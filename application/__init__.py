from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

''' Database connections '''
app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from application import routes


if __name__ == '__main__':
    app.run(debug=False)
