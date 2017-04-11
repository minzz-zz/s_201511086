
from pymongo import MongoClient

client = MongoClient()
db = client.myDB

_id=1
_name="mj"
_age=22
_country="ko"

db.myPyCol.insert_one({
    "id" : _id,
    "name" : _name,
    "age" : _age,
    "country" : _country
})

results = db.myPyCol.find()
for r in results:
    print r['name']
    
_name = "mjkim"
_age = 20

db.myPyCol.update_one(
    {"id" : _id},
    {
        "$set" : {
            "name": _name,
            "age": _age,
        }
    }
)

results = db.myPyCol.find()
for r in results:
    print r['id'], r['name']

db.myPyCol.delete_many({"id":1})

results = db.myPyCol.find()
for r in results:
    print r['id'], r['name']