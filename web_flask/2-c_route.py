#!/usr/bin/python3
'''A simple Flask web application'''
from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
