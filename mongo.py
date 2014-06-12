from pymongo import MongoClient


class Mongo():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.test

    def populate(self):
        self.db.things.remove()
        things = [
            {"name": "Vishnu"},
            {"name": "Lakshmi"},
            {"name": "Ganesha"},
            {"name": "Krishna"},
            {"name": "Murugan"}
        ]
        self.db.things.insert(things)

    def count(self):
        return self.db.things.count()

if __name__ == "__main__":
    mongo = Mongo()
    mongo.populate()
    print(mongo.count())
