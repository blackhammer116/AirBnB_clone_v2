#!/usr/bin/python3
"""
  importing our flask framework
"""
from flask import Flask


app = Flask(__name__)
strict_slashes=False

@app.route('/', strict_slashes=False)
def Hello_HBHB():
  return "Hello HBNB!"

if __name__ == '__main__':
  app.run(host = '0.0.0.0',port = 5000)