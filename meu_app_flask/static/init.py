# app/__init__.py

from flask import Flask

app = Flask(__name__)

from meu_app_flask.app import routes