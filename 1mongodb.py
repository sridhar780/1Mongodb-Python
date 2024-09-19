#pip install pymongo
from pymongo import MongoClient

# Replace the URI string with your MongoDB deployment's connection string.
client = MongoClient("mongodb://localhost:27017/")

# Access the database
db = client["tcsdb"]

# Access a collection
collection = db["developer"]

# Print a success message
print("Connected to MongoDB successfully!")


# Insert a document
document = {"name": "Madhu", "age": 30, "city": "Hyderbad"}
collection.insert_one(document)

# Find a document
result = collection.find_one({"name": "Madhu"})
print(result)
