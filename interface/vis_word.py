from flask import Flask, request
from flask import json
from flask import send_from_directory
from flask import render_template
import sys
sys.path.append('../trainer')
from trainer import Trainer
app = Flask(__name__,static_url_path='')

new_trainer = Trainer()
@app.route('/')
def index():
    return render_template('index_network.html')

def to_id(x):
    a = 0
    for i in xrange(len(x)):
        if x[i]:
            a += 1
    return a

@app.route('/data/<string:pere>')
def get_data(pere):
    plist = [int(x) for x in pere.split()]
    return json.dumps(new_trainer.get_data(to_id(plist)))

@app.route('/lazy.js')
def get_path():
    return app.send_static_file('lazy.js')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8888
    print port
    app.run(port=port)
