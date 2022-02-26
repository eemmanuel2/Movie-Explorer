# pylint: disable=warning codes, warnings code, more warnings codes
import os
import random
import requests
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env


def movie_id_search():
    params = {"api_key": os.getenv("TMDB_KEY")}

    BASE_URL = "https://api.themoviedb.org/3/movie/"
    movies = [566525, 370172, 634649, 476669, 351346]
    a = random.randrange(0, len(movies) - 1)
    movie_id = movies[a]
    BASE_URL = BASE_URL + str(movie_id)

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    movieList = data

    moviename = movieList["title"]
    movietag = movieList["tagline"]
    moviepicture = movieList["poster_path"]
    moviegenre = " , ".join([genre["name"] for genre in movieList["genres"]])
    piclink = "https://image.tmdb.org/t/p/w500/"
    movi_id = movieList["id"]

    URL = "https://en.wikipedia.org/w/api.php"

    # movietitle = movie_id_search()
    # c = movieList['moviename']

    params = {
        "action": "query",
        "format": "json",
        "titles": moviename,
        "prop": "info",
        "inprop": "url|talkid",
    }

    response = requests.get(URL, params=params)

    tri = response.json()["query"]["pages"]
    wiki = tri[(list(tri.keys())[0])]["canonicalurl"]
    # link = tri["query"]["pages"][a]["canonicalurl"]
    print(moviename, movietag, moviepicture, moviegenre, piclink, wiki, movi_id)

    # FAITH IS A GENIUS FIXED WIKIPEDIA

    return {
        "moviename": (moviename),
        "movietag": (movietag),
        "moviepicture": (moviepicture),
        "piclink": (piclink),
        "moviegenre": (moviegenre),
        "wiki": (wiki),
        "movi_id": (movi_id),
    }


movie_id_search()
