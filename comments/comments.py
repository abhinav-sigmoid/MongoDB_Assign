# 1. Find top 10 users who made the maximum number of comments 

db.getCollection('comments').aggregate([
    {"$group": {"_id": {"User's_name": "$name", "email_id": "$email"}, "TotalComments": {"$sum": 1}}},
    {"$sort": {"TotalComments": -1}},
    {"$limit": 10}
])

# 2. Find top 10 movies with most comments

db.getCollection('comments').aggregate([
    {"$group": {"_id": {"Movie's_name": "$movie_id"}, "TotalComments": {"$sum": 1}}},
    {"$sort": {"TotalComments": -1}},
    {"$limit": 10}
])


# 3. Given a year find the total number of comments created each month in that year


