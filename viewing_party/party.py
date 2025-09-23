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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

