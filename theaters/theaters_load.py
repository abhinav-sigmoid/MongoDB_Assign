import pymongo
import json
from bson import ObjectId

# Establishing the connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mflix"]
theaters = mydb["theaters"]

# Loading Data
item_list = []
with open("theaters.json") as f:
    for json_obj in f:
        if json_obj:
            my_dict = json.loads(json_obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            my_dict["theaterId"] = int(my_dict["theaterId"]["$numberInt"])
            try:
                my_dict["location"]["geo"]["coordinates"] = [
                    float(my_dict["location"]["geo"]["coordinates"][0]["$numberDouble"]),
                    float(my_dict["location"]["geo"]["coordinates"][1]["$numberDouble"])]
            except:
                pass
            item_list.append(my_dict)

# Inserting to Database
theaters.insert_many(item_list)