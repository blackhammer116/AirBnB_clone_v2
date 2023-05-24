#!/usr/bin/python3
"""
  importing our flask framework
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBHB():
""" displaying hello HBNB """
  return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
""" displaying HBNB """
  return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
""" displaying the text replacing _ with a space
    Args:
       text: text to be printed
"""
  return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
""" displaying the python text
    Args:
       text: text to be printed
"""
  return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
""" displaying n
    Args:
       n: number to be printed
"""
  return '{} is a number'.format(n)


if __name__ == '__main__':
  app.run(host = '0.0.0.0',port = 5000, debug=True)
