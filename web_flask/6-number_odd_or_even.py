#!/usr/bin/python3
'''A simple Flask web application'''
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''Route for the root URL'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Route for the /hbnb URL'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    '''Route for the /c/<text> URL'''
    # Replace underscores with spaces and escape the text
    safe_text = escape(text).replace('_', ' ')
    return f"C {safe_text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python(text="is cool"):
    '''Route for the /python/<text> URL'''
    # Replace underscores with spaces and escape the text
    safe_text = escape(text).replace('_', ' ')
    return f"Python {safe_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''Route for the /number/<n> URL'''
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    '''Route for the /number_template/<n> URL'''
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_html_odd_even(n):
    '''Route for the /number_template/<n> URL'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
