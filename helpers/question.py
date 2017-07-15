import random
from .db import DatabaseManager


questions = DatabaseManager.get_client().questions


class Question(object):
    def __init__(self,question,anwsers):
        """Create a Question ins.

        arguments:
        - question: str
        - anwsers: tuple, (true_anwser,[false_answers...])
        """
        self.question = question
        self.true_anwser = anwsers[0]
        self.false_answers = anwsers[1]

    def save(self):
        """Save question to database
        struct:
        {
            id: int
            question: str,
            true: str,
            falses: [str...]
        }
        """
        questions.insert({
            "id": questions.count() + 1,
            "question": self.question,
            "true": self.true_anwser,
            "falses": self.false_answers
        })

    @classmethod
    def random_one(cls, num_of_qu=None):
        if not num_of_qu:
            num_of_qu = questions.count()
        doc = questions.find_one({"id": random.randint(1, num_of_qu)})
        if doc:
            return cls(doc.question, (doc.true, doc.falses))
        else:
            return None

    @classmethod
    def random(cls, num=25):
        for x in range(1, 25):
            yield cls.random_one(num_of_qu=questions.count())

    @classmethod
    def find(cls, question):
        doc = questions.find_one({"question":question})
        return cls(doc.question, (doc.true, doc.falses))

    @staticmethod
    def unpack(q):
        answers = q.false_answers.copy().insert(
            random.randint(0, 2), q.true_anwser
            )
        return q.question, answers
