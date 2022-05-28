#!/usr/bin/python3
""" script that starts a Flask web application"""


from flask import Flask, request


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello2():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello3():
    text_input = request.get("text")
    for character in text_input:
        if character == "_":
            character == " "
    return 'C' + text_input


if __name__ == '__man__':
    app.run(host='0.0.0.0', port=5000)
