#!/usr/bin/python3
'''Base model'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''function that returns Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''function that returns HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''function that print text variable'''
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    '''function that print text variable'''
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
