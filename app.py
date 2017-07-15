
from tornado.web import Application

from handlers.verify import VerifyHandler


route_mapping = [
        (r"/verify", VerifyHandler)
        ]


config = {
        "debug": True
        }

def get_app():
    return Application(route_mapping,config)
