from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from typing import Dict, Any, List


def filter_documents(
        collection: Collection,
        filter_criteria: list,
        sort_criteria: dict,
        project_fields: dict,
        group_by_fields: dict,
        match_criteria2: dict,
) -> Cursor:
    pipeline = [
        {
            '$match': {
                '$and': filter_criteria
            },
        },
        {
            '$sort': sort_criteria
        },
        {
            "$project": project_fields
        },
        # {
        #     "$unwind": "$tags"
        # }
        {
            "$group": group_by_fields
        },
        {
            "$match": match_criteria2
        },
        {
            "$project": {"average_qty": 0}
        }

    ]
    return collection.aggregate(pipeline)

# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017')
db = client['new2']
collection = db['inventory']

# Define the filter criteria
filter_criteria: List[Dict[str, Any]] = [
    # {'item': "journal"},
    # {'$or': [{'status': 'A'}, {'status': 'D'}]},
    {'qty': {'$not': {'$gt': 75}}}
]

sort_criteria = {"item": -1, "qty": 1}

# project_fields = {"item": 1, "qty": 1, "_id": 0, "instock.warehouse": 1, "status": 1}

project_fields = {"item": 1, "qty": 1, "_id": 0, "instock.warehouse": 1, "status": 1, "tags": 1}

group_by_fields = {"_id": {"status": "$status", "item": "$item"}, "count": {"$sum": 1}, 'sum_qty': {"$sum": "$qty"}}

match_criteria2 = {"sum_qty": {"$gt": 40}}

# Call the filter_documents function
result = filter_documents(collection, filter_criteria, sort_criteria, project_fields, group_by_fields, match_criteria2)

# Iterate over the cursor and print the filtered documents
for doc in result:
    print(doc)