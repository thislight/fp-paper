"""Some helpers of database
"""
import os
from pymongo import MongoClient


DEFAULTMONGOURL = "mongodb://localhost"


class DatabaseManager(object):
    _client = None

    @classmethod
    def get_client(cls):
        """Get a `Database` of app
        """
        if not cls._client:
            cls._client = MongoClient(cls.get_uri())["reg-exam"]
        return cls._client

    @staticmethod
    def get_uri():
        return os.environ.get("PFPAPER_MONGO",default=DEFAULTMONGOURL)
