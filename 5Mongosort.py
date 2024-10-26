import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ssgi"]
mycol = mydb["ssdc"]

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)
