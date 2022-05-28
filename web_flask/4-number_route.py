#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text='is cool'):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    if type(int(n)) == int:
        return n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
