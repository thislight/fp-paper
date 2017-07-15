
from pymongo import MongoClient

MONGOURL="mongo://localhost/reg-exam"

class DatabaseManager(object):
    _client = None
    @classmethod
    def get_client(cls):
        if not cls._client:
            cls._client = MongoClient(MONGOURL)
        return cls._client
