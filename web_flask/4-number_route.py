#!/usr/bin/python3
"""
starts a Flask web application with routes and variables
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB"


@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", methods=['GET'], strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)