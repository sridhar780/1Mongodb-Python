import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ssgi"]
mycol = mydb["ssdc"]

mycol.drop()
