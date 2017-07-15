
import os.path
from tornado.web import Application

from handlers.asking import PaperHandler
from handlers.verify import VerifyHandler


route_mapping = [
        (r"/verify", VerifyHandler),
        (r"/paper", PaperHandler)
        ]


config = {
        "debug": True,
        "template_path": os.path.join(".", "templates"),
        "static_path": os.path.join(".", "static")
        }

def get_app():
    return Application(route_mapping, **config)
