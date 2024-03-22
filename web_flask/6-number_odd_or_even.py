#!/usr/bin/python3
'''Base model'''
from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''function that print text variable'''
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    '''display n if is anumber'''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    '''return html page'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    '''return html page'''
    return render_template('6-number_odd_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
