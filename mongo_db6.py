from pymongo import MongoClient
from pymongo.errors import OperationFailure, PyMongoError


def update_document(database_name: str, collection_name: str, filter_query: dict, update_query: dict) -> bool:
    try:
        # Connect to MongoDB
        client: MongoClient = MongoClient('mongodb://localhost:27017')
        db = client[database_name]
        collection = db[collection_name]

        client.close()

        # Perform the update operation
        result = collection.update_one(filter_query, update_query)

        # Close the MongoDB connection
        client.close()

        if result.modified_count > 0:
            return True
        else:
            return False

    except OperationFailure as e:
        print('Operation failure:', str(e))
        return False

    except PyMongoError as e:
        print('An error occurred:', str(e))
        return False


# Usage
database_name = 'mydatabase'
collection_name = 'mycollection'
filter_query = {'name': 'John'}
update_query = {'$set': {'age': 30}}

if update_document(database_name, collection_name, filter_query, update_query):
    print('Document updated successfully.')
else:
    print('Failed to update document.')