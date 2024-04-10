from pymongo import MongoClient
from pymongo.errors import PyMongoError


def query_database() -> None:
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017')
        db = client['mydatabase']
        collection = db['mycollection']

        # Perform a query
        result = collection.find_one({'name': 'John'})

        # Process the result
        if result:
            print('Found document:', result)
        else:
            print('Document not found.')

        # Close the MongoDB connection
        client.close()

    except PyMongoError as e:
        print('An error occurred:', str(e))


# Call the function
query_database()
