from flask import Flask
from flask import json
from flask import render_template
import sys
sys.path.append('../trainer')
from trainer import Trainer
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index_network.html')


@app.route('/data')
def get_data():
    return 

def hello():
    return 'Hello!'

if __name__ == '__main__':
      app.run(port=8888)