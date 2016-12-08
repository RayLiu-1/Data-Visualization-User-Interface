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

data1 = {
    "edges" : [
        {"from": "2", "to": "8", "value": "3"},
        {"from": "2", "to": "9", "value": "5"},
        {"from": "2", "to": "10","value": "1"},
        {"from": "4", "to": "6", "value": "8"},
        {"from": "5", "to": "7", "value": "2"},
        {"from":"4", "to": "5", "value": "1"},
        {"from": "9", "to": "10","value": "2"},
        {"from": "2", "to": "3", "value": "6"},
        {"from": "3", "to": "9", "value": "4"},
        {"from": "5", "to": "3", "value": "1"},
        {"from": "2", "to": "7", "value": "4"}
      ],

  "nodes" : [
        {"id": "1",  "value": "2",  "label": "Algie"},
        {"id": "2",  "value": "31", "label": "Alston"},
        {"id": "3",  "value": "1", "label": "Barney"},
        {"id": "4",  "value": "16", "label": "Coley" },
        {"id": "5",  "value": "1", "label": "Grant" },
        {"id": "6",  "value": "15", "label": "Langdon"},
        {"id":"7",  "value": "6",  "label": "Lee"},
        {"id": "8",  "value": "5",  "label": "Merlin"},
        {"id": "9",  "value": "30", "label": "Mick"},
        {"id": "10", "value": "18", "label": "Tod"},
      ]
  }


@app.route('/data/<pere>')
def get_data(pere):
    return json.dumps(new_trainer.get_data(1))

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
