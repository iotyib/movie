# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello ffae!'
from app import app

if __name__ == '__main__':
    app.run()
