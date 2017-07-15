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
        self.papers = DatabaseManager.get_client().papers

    def _get_questions(self):
        return [v for v in Question.random(20)]

    def get_questions(self):
        quz = self._get_questions()
        true_answers = [ q.true_answer for q in quz ]
        paper_id = secrets.token_urlsafe()
        self.set_secret_cookie("paper_id",paper_id)
        self.papers.insert({
            "id": paper_id,
            "answers": true_answers
            })
        n = -1
        for q in quz:
            n += 1
            yield n, *(Question.unpack(q))

    def get(self):
        self.render(
            "asking.html",
            get_questions=self.get_questions,
            )

    def get_marks(self, answers):
        paperid = self.get_secret_cookie("paper_id")
        true_answers = self.paper.find_one({
            "paper_id":paperid
            })["answers"]
        mark = 0
        n = -1
        for user_answer in answers:
            n += 1
            if user_answer == true_anwsers[n]:
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
                "redirect": "/result/fail",
                "error": "mark is lower than 60",
                "mark": mark
            })
