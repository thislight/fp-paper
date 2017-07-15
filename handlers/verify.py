
from tornado.web import RequestHandler
from helpers.db import DatabaseManager


class VerifyHandler(RequestHandler):
    def initialize(self):
        self.emails = DatabaseManager.get_client().emails

    def get(self):
        email = self.get_argument(
                "email",
                default=None
                )
        if not email:
            return {
                    "ok": 1,
                    "email": email,
                    "error": "field email is empty"
                    }
        result = self.emails.find({
            "email": email
            }).count()
        if result > 0:
            return {
                    "ok": 0,
                    "email": email
                    }
        else:
            return {
                    "ok": 2,
                    "email": email,
                    "error": "email don't pass exam"
                    }

