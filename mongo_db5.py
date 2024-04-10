import time

from pymongo import MongoClient
from pymongo.errors import ExecutionTimeout, PyMongoError
from random_word import RandomWords


# def query_with_timeout(database_name: str, collection_name: str, query: dict, timeout_ms: int) -> list:
#     try:
#         # Connect to MongoDB
#         client: MongoClient = MongoClient('mongodb://localhost:27017')
#         db = client[database_name]
#         collection = db[collection_name]
#
#         # Set query options with timeout
#         query_options = {'$query': query, '$maxTimeMS': timeout_ms}
#
#         # Perform the query
#         result = list(collection.find(query_options))
#
#         # Close the MongoDB connection
#         client.close()
#
#         return result
#
#     except ExecutionTimeout as e:
#         print('Query execution timeout:', str(e))
#         return []
#
#     except PyMongoError as e:
#         print('An error occurred:', str(e))
#         return []


# Usage
database_name = 'new2'
collection_name = 'col3'


client: MongoClient = MongoClient('mongodb://localhost:27017')
db = client[database_name]
collection = db[collection_name]
query = {}
r = RandomWords()
# for i in range(1000):
#     collection.insert_one({"barcode": i+200, "name": r.get_random_word(), "name2": r.get_random_word()})

start = time.time()
for i in range(1000):
    collection.find_one({"name": "aholds"})
end = time.time()
delta = end - start

print(delta)

start = time.time()
for i in range(1000):
    collection.find_one({"name2": "countree"})
end = time.time()
delta = end - start

print(delta)

# query = {'name': 'John'}
# timeout_ms = 1
#
# query_result = query_with_timeout(database_name, collection_name, query, timeout_ms)
#
# if query_result:
#     print('Query result:', query_result)
# else:
#     print('No results or error occurred during the query.')