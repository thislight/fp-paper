"""
Handler for asking page
"""

import secrets
import json as json
from helpers.question import Question
from helpers.db import DatabaseManager
from tornado.web import RequestHandler


MARK_OF_ONE_QUESTION = 5


class PaperHandler(RequestHandler):
    def initialize(self):
        self.codes = DatabaseManager.get_client().codes
    
    def get_questions(self):
        n = 0
        for q in Question.random(20):
            yield n, Question.unpack(q)
            n += 1

    def get(self):
        self.render(
            "asking.html",
            get_questions=self.get_questions,
            )
    
    def get_marks(self, answers):
        mark = 0
        for answer in answers:
            question = answer["question"]
            user_answer = answer["answer"]
            q = Question.find(question)
            if user_answer == q.true_anwser:
                mark += MARK_OF_ONE_QUESTION
        return mark
    
    def post(self):
        req = json.loads(self.request.body)
        mark = self.get_marks(req["answers"])
        if mark > 12*MARK_OF_ONE_QUESTION:
            code = secrets.token_urlsafe()
            self.codes.insert({
                "code": code
            })
            self.write({
                "ok": 0,
                "redirect": "/result/done?code={}".format(code),
                "mark": mark
            })
        else:
            self.write({
                "ok": 1,
                "error": "mark is lower than 60",
                "mark": mark
            })