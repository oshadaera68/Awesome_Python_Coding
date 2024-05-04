from bson.objectid import ObjectId
from bson.son import SON
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client.neuraldb

people = db.people

mike_id = people.insert_one({"name": "Mike", "age": 30})
people.insert_one({"name": "Lisa", "age": 20, "interests": ["C++", "Python", "Piano"]})
mike_id = people.insert_one({"name": "Mike", "age": 40})
mike_id = people.insert_one({"name": "Mike", "age": 27})
people.insert_one({"name": "Lisa", "age": 26, "interests": ["C++", "Python", "Piano"]})
people.insert_one({"name": "Lisa", "age": 78})

for person in people.find():
    print(person)

print([p for p in people.find({'_id': ObjectId('66357f1c034c2671ecae46e6')})])
print([p for p in people.find({"age": {"$lt": 25}})])

print(people.count_documents({"name": "lisa"}))
people.update_one({"_id": ObjectId('66357f1c034c2671ecae46e7')}, {"$set": {"age": 27}})

people.delete_many({"age": {"$lt": 37}})

pipline = [
    {
        "$group": {
            "_id": "$name",
            "averageAge": {"$avg": "$age"},
        }
    },
    {
        "$sort": SON([("averageAge", -1), ("_id", -1)]),
    }
]

results = people.aggregate(pipline)

for result in results:
    print(result)
