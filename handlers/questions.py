import json as json
from helpers.question import Question
from tornado.web import RequestHandler
from helpers.db import DatabaseManager


class QuestionHandler(object):
    def initialize(self):
        self.questions = DatabaseManager.get_client().questions

    def post(self):
        req = json.loads(self.request.body)
        if Question.find(req["question"]):
            self.write({
                "ok": 1,
                "error": "question has been in database"
                })
            return
        Question(
                req["question"],
                (
                    req["true"],
                    req["falses"]
                    )
                ).save()
        self.write({
            "ok":0
            })

