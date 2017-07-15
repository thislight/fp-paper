
from tornado.web import RequestHandler
from helpers.db import DatabaseManager


class VerifyHandler(RequestHandler):
    def initialize(self):
        self.codes = DatabaseManager.get_client().codes

    def get(self):
        """Verify a code that in database
        Usage:
        GET https://example.com/verify?code=example

        if passed:
            {
                "ok":0,
                "code":"example"
            }
        if not 'code'(such as '/verify'):
            {
                "ok": 1,
                "code": "example",
                "error": "argument code is empty"
            }
        if 'code' not found in database:
            {
                "ok": 2,
                "code": "example",
                "error": "code not found"
            }
        """
        code = self.get_argument(
                "code",
                default=None
                )
        if not code:
            self.write({
                    "ok": 1,
                    "code": code,
                    "error": "argument code is empty"
                    })
        result = self.codes.find({
            "code": code
            }).count()
        if result > 0:
            self.write({
                    "ok": 0,
                    "code": code
                    })
        else:
            self.write({
                    "ok": 2,
                    "code": code,
                    "error": "code not found"
                    })

