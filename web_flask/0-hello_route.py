#!/usr/bin/python3
'''A simple Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_Hbnb():
    '''Route for the root URL'''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
