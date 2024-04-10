from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict

from pymongo.errors import ServerSelectionTimeoutError


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database

mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'new2'
collection_name = 'inventory'

try:
    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)



    # Retrieve a specific collection
    collection = db[collection_name]

    # Delete Operation
    query = {"name": "John Doe"}

    result = collection.find_one( {"qty": 85}, { "tags": 1, "size": 1})
    print(result)

    result = collection.find({"qty": {"$eq": 25}})
    for item in result:
        print("QTYYY", item["qty"])

    print("NOT EQUALS 25")

    result = collection.find({"qty": {"$ne": 25}})
    for item in result:
        print(item)

    print("GREATER THAN 25")

    result = collection.find({"qty": {"$gt": 25}})
    for item in result:
        print(item)

    print("LESS THAN 25")

    result = collection.find({"qty": {"$lt": 25}})
    for item in result:
        print(item)

    print("GREATER THAN OR EQUAL 25")

    result = collection.find({"qty": {"$gte": 25}})
    for item in result:
        print(item)

    print("LESS THAN OR EQUAL 25")

    result = collection.find({"qty": {"$lte": 25}})
    for item in result:
        print(item)

    quarters = [25, 50, 75, 100]

    result = collection.find({"qty": {"$in": quarters}})

    print("IN QUARTERS")

    for item in result:
        print(item)

    result = collection.find({"qty": {"$nin": quarters}})

    print("NOT IN QUARTERS")

    for item in result:
        print(item)

except ServerSelectionTimeoutError:
    print("no connection")
