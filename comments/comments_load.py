import json

import pymongo
from pymongo import MongoClient
from bson import ObjectId

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
except:
    print("Error in Connect")

db = myclient['study']

comments = db['comments']

item_list = []

with open('comments.json') as f:
    for json_obj in f:
        if json_obj:
            my_dict = json.loads(json_obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            my_dict["date"] = my_dict["date"]["$date"]["$numberLong"]
            item_list.append(my_dict)

comments.insert_many(item_list)

# db.comments.find({})
