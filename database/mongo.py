from pymongo import MongoClient
from bson import json_util
import json
#mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false

class Mongo:
    def __init__(self, client, collection):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client[client]
        self.collection = self.db[collection]

    def find_all(self):
        r = []
        for i in self.collection.find():
            r.append(json.loads(json_util.dumps(i)))
        return r

    def find(self, query):
        r = []
        for i in self.collection.find(query):
            r.append(json.loads(json_util.dumps(i)))
        return r

    def find_one(self, query):
        r = self.collection.find_one(query)
        return json.loads(json_util.dumps(r))

    def insert_one(self, data):
        return self.collection.insert_one(data)

    def insert_many(self, data):
        return self.collection.insert_many(data)

    def update(self, query, newValue):
        return self.collection.update_many(query, {"$set": newValue})

    def update_one_custom(self, query, custom):
        return self.collection.update_one(query, custom)

    def update_many_custom(self, query, custom):
        return self.collection.update_many(query, custom)

    def delete_one(self, query):
        return self.collection.delete_one(query)

    def delete_many(self, query):
        return self.collection.delete_many(query)

    def drop(self):
        return self.collection.drop()


