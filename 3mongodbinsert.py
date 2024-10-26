import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ssgi"]
mycol = mydb["ssdc"]

x = mycol.find_one()

print(x)
