from tornado.web import RequestHandler

class ResultDoneHandler(RequestHandler):
    def get(self):
        self.render("done.html",code=self.get_argument("code"))


class ResultFailHandler(RequestHandler):
    def get(self):
        self.render("fail.html")
