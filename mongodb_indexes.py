from pymongo import MongoClient

client: MongoClient = MongoClient('mongodb://localhost:27017')
db = client["new2"]
collection = db["col3"]

collection.create_index("barcode", unique=True)

collection.create_index("name")
