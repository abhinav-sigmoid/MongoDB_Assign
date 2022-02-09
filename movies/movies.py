# 1.	Find top `N` movies - 

# 1.1.	with the highest IMDB rating

db.getCollection('movies').aggregate([
        {"$project": {"title": 1, "imdb.rating": 1}},
        {"$sort": {"imdb.rating": -1}},
        {"$limit": 10}
    ])
    
# 1.2.	with the highest IMDB rating in a given year

db.getCollection('movies').aggregate([
        {"$match": {"year": 1914}},
        {"$project": {"_id": 0, "title": 1, "imdb.rating": 1}},
        {"$sort": {"imdb.rating": -1}},
        {"$limit": 10}
    ])
    
# 1.3	with highest IMDB rating with number of votes > 1000

db.getCollection('movies').aggregate([
        {"$match": {"imdb.votes": {"$gt": 1000}}},
        {"$project": {"_id": 0, "imdb.votes":1, "title": 1, "imdb.rating": 1}},
        {"$sort": {"imdb.rating": -1}},
        {"$limit": 10}
    ])
    
# 1.4	with title matching a given pattern sorted by highest tomatoes ratings

db.getCollection('movies').aggregate([
        {"$match": {"title": {"$regex": "Scene"}}},
        {"$project": {"_id": 0, "title": 1, "tomatoes.viewer.rating": 1}},
        {"$sort": {"tomatoes.viewer.rating": -1}},
        {"$limit": 10}
    ])
    


# 2.	Find top `N` directors -

# 2.1 	who created the maximum number of movies

db.getCollection('movies').aggregate([
        {"$unwind": "$directors"},
        {"$group": {"_id": {"Directors": "$directors"}, "TotalMovies": {"$sum": 1}}},
        {"$sort": {"TotalMovies": -1}},
        {"$limit": 10}
    ])
    
    
# 2.2 	who created the maximum number of movies in a given year

db.getCollection('movies').aggregate([
        {"$unwind": "$directors"},
        {"$group": {"_id": {"directors": "$directors", "year": "$year"}, "TotalMovies": {"$sum": 1}}},
        {"$sort": {"TotalMovies": -1}},
        {"$match": {"_id.year": 1911}},
        {"$project": {"_id.directors": 1, "TotalMovies": 1}},
        {"$limit": 10}
    ])
    
    
# 2.3	who created the maximum number of movies for a given genre

db.getCollection('movies').aggregate([
        {"$unwind": "$directors"},
        {"$unwind": "$genres"},
        {"$group": {"_id": {"directors": "$directors", "genres": "$genres"}, "totalMovies": {"$sum": 1}}},
        {"$sort": {"totalMovies": -1}},
        {"$match": {"_id.genres": "Short"}},
        {"$project": {"totalMovies": 1}},
        {"$limit": 10}
    ])


# 3.	Find top `N` actors - 

# 3.1	who starred in the maximum number of movies

db.getCollection('movies').aggregate([
        {"$unwind": "$cast"},
        {"$group": {"_id": {"cast": "$cast"}, "totalMovies": {"$sum": 1}}},
        {"$sort": {"totalMovies": -1}},
        {"$limit": 10}
    ])
    
    
# 3.2 	who starred in the maximum number of movies in a given year

db.getCollection('movies').aggregate([
        {"$unwind": "$cast"},
        {"$group": {"_id": {"cast": "$cast", "year": "$year"}, "totalMovies": {"$sum": 1}}},
        {"$sort": {"totalMovies": -1}},
        {"$match": {"_id.year": 1912}},
        {"$project": {"_id.year": 0}},
        {"$limit": 10}
    ])
    
    
# 3.3	who starred in the maximum number of movies for a given genre

db.getCollection('movies').aggregate([
        {"$unwind": "$cast"},
        {"$unwind": "$genres"},
        {"$group": {"_id": {"cast": "$cast", "genres": "$genres"}, "totalMovies": {"$sum": 1}}},
        {"$sort": {"totalMovies": -1}},
        {"$match": {"_id.genres": 'Short'}},
        {"$limit": 10}
    ])
    
    
# 4. 	Find top `N` movies for each genre with the highest IMDB rating






