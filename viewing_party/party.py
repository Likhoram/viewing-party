# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
# if title or genre or rating is false, return None
    if not title or not genre or not rating:
        return None 

# if inputs are true, return dictionary{title: ; genre: ; rating: }
    # movie = {}
    # movie["title"] = title
    # movie["genre"] = genre
    # movie["rating"] = rating

    movie = {
        "title" : title,
        "genre": genre,
        "rating": rating
    }
    return movie

def add_to_watched(user_data, movie):
# user_data = {watched: [{}]}, if no movies watched, then empty list.
# movie =  {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
# add movie to watched in user_data. Return user_data.

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
# user_data = {watchlist: [{}]}, if no movies in watchlist, then empty list.
# movie =  {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
# add movie to watchlist in user_data. Return user_data.

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
# user_data = {watchlist: ; watched: }
# title = "movie user has watched"
# if title is in watchlist, remove from watchlist, add to watched, return user_data.
# if title not in watchlist, return user_data.

    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    average_rating = 0.0

    if not user_data:
        return average_rating
    
    for movie in user_data:
        rating += user_data["rating"]
    
    average_rating = rating / len(user_data)
    return average_rating

def get_most_watched_genre(user_data):
    
    if not user_data:
        return None
    
    genre_dict = {}

    for movie in user_data:
        for genre in movie["genre"]:
            if genre in genre_dict:
                genre_dict[genre] += 1
            else:
                genre_dict[genre_dict] = 1
        
    most_frequent_movie = None
    highest_counter = 0

    for i in range(genre_dict):
        if genre_dict["genre"] > highest_counter:
            most_frequent_movie = genre_dict.keys[i]

    return most_frequent_movie


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# movie =  {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
def get_unique_watched(user_data):
# user_data = {"watched": [{}], "friends": [{"watched":[{}]}]}
# return movie user has watched but friends haven't as a list of dictionaries
# compare {} in "watched" and "friends":"watched", return the unique one in "watched".

# make a list of friends wathced movie titles.
    friends_movies = []
    for movie_dict in user_data["friends"]:
        for movie in movie_dict["watched"]:
            friends_movies.append(movie["title"])

# loop throught user watched list, return ones different than friends watched list.
    user_unique = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movies:
            user_unique.append(movie)

    return user_unique       

def get_friends_unique_watched(user_data):
# return movie at least one of the friends have watched, but user hasn't as a list of dict
    user_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie["title"])

    friends_unique = []
    for movie_dict in user_data["friends"]:
        for movie in movie_dict["watched"]:
            if movie["title"] not in user_movies:
                friends_unique.append(movie)

    return friends_unique
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    
