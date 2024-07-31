#!/usr/bin/python3
"""
Starts a Flask web application with multiple routes.
"""

from flask import Flask
import html

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB!'."""
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns 'C <text>' where <text> is a URL parameter
    with underscores replaced by spaces."""
    txt = text.replace('_', ' ')
    return "C {}".format(html.escape(txt))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
