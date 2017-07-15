from app import get_app
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


def get_server():
    return HTTPServer(get_app())


def start(port=8088, workers=1, address="127.0.0.1"):
    server = get_server()
    server.bind(port,address=address)
    try:
        server.start(workers)
        IOLoop.current().start()
    except Exception as e:
        server.stop()
        IOLoop.current().stop()


def __main__():
    start()


if __name__ == "__main__":
    __main__()
