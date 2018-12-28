import requests
from .api_movie_parser import parse as parse_movie
from movies.characters.api_character_parser import parse as parse_character


MOVIE_LIST_PATH = 'https://ghibliapi.herokuapp.com/films'
CHARACTERS_PATH = 'https://ghibliapi.herokuapp.com/people'


def find_movies():
    response = requests.get(MOVIE_LIST_PATH)
    if response.ok:
        return list(map(parse_movie, response.json()))
    else:
        return []


def find_characters(movie_id):
    response = requests.get(CHARACTERS_PATH, params={
        'film': movie_id
    })

    if response.ok:
        return list(map(parse_character, response.json()))
    else:
        return []
