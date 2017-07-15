
import os.path
from tornado.web import Application

from handlers.asking import PaperHandler
from handlers.verify import VerifyHandler
from handlers.questions import QuestionHandler


route_mapping = [
        (r"/verify", VerifyHandler),
        (r"/paper", PaperHandler),
        (r"/questions/add",QuestionHandler)
        ]


config = {
        "debug": True,
        "template_path": os.path.join(".", "templates"),
        "static_path": os.path.join(".", "static")
        }

def get_app():
    return Application(route_mapping, **config)
