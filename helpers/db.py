"""Some helpers of database
"""
from pymongo import MongoClient


MONGOURL = "mongodb://localhost"


class DatabaseManager(object):
    _client = None

    @classmethod
    def get_client(cls):
        """Get a `Database` of app
        """
        if not cls._client:
            cls._client = MongoClient(MONGOURL)["reg-exam"]
        return cls._client
