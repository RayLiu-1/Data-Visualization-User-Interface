from flask import Flask
from flask import render_template
from trainer import Trainer
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/help')
def hello():
    return 'Hello!'
