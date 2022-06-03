# wsgi.py
### heroku create myapp --buildpack heroku/python
# pylint: disable=missing-docstring

from flask import Flask
app = Flask(__name__)

PRODUCTS = {
    1: {
        'id': 1,
        'name': 'Skello'
    },
    2: {
        'id': 2,
        'name': 'Socialive.tv'
    },
    3: {
        'id': 3,
        'name': 'Le Wagon'
    },
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def api():
    return PRODUCTS
