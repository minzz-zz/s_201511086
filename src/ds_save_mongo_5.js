use myDB
show dbs
show tables
db.myCol.insert({"Persons":[{"id":"405", "�̸�":"js1"},{"id":"406", "�̸�":"js2"}]})
db.myCol.find({ "Persons.�̸�": "js1" })