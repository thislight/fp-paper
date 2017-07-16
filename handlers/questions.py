import json as json
from helpers.question import Question
from tornado.web import RequestHandler
from helpers.db import DatabaseManager


class QuestionAddHandler(object):
    def initialize(self):
        self.questions = DatabaseManager.get_client().questions

    def post(self):
        req = json.loads(self.request.body)
        if self.questions.find_one({ "question": req["question"] }):
            self.write({
                "ok": 1,
                "error": "question has been in database"
                })
            return None
        self.questions.insert({
            "question":req["question"],
            "true":req["true"],
            "falses":list(req["falses"])
            })
        self.write({
            "ok":0
            })

