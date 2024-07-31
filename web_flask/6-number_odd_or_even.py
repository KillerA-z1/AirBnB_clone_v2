#!/usr/bin/python3
"""
Starts a Flask web application with routes for displaying number information.
"""

from flask import Flask, render_template
import html  # For escaping HTML

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
    """Returns 'C <text>' where <text> is a URL parameter with underscores
    replaced by spaces."""
    txt = text.replace('_', ' ')
    return "C {}".format(html.escape(txt))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_is_fun(text):
    """Returns 'Python <text>' where <text> is a URL parameter with underscores
    replaced by spaces. Defaults to 'is cool'."""
    txt = text.replace('_', ' ')
    return "Python {}".format(html.escape(txt))


@app.route('/number/<int:n>', strict_slashes=False)
def number_is_num(n):
    """Returns '<n> is a number' if <n> is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_n_to_template(n):
    """Renders a template with the integer <n>."""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_odd_or_even(n):
    """Renders a template with 'even' or 'odd' based on the integer <n>."""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
