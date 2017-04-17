
from pymongo import MongoClient

p1 = {"id" : "405", "name" : "js1"}
p2 = {"id" : "406", "name" : "js2"}
p={"Persons":[p1, p2,]}

client = MongoClient()
db = client.myDB
db.myCol.drop()
db.myCol.insert_one(p)

result = db.myCol.find()
for r in result:
    print r["Persons"]