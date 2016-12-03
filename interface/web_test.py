import tornado.ioloop
import tornado.web
import sys
sys.path.append('../trainer')
from trainer import Trainer


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class DataHandler(tornado.web.RequestHandler):
    def initialize(self, trainer):
        self.trainer = trainer

    def get(self):
        self.write(self.trainer.get_data())

class UserHandler(tornado.web.RequestHandler):
    def post(self):
        data = self.get_argument('query')
        print(data)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/data", DataHandler, {'trainer': Trainer()}),
        (r"/user", UserHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

