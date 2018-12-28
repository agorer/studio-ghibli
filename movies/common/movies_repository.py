import requests
from .api_movie_parser import parse as parse_movie
from movies.characters.api_character_parser import parse as parse_character


class MoviesRepository:
    MOVIE_LIST_PATH = 'https://ghibliapi.herokuapp.com/films'
    CHARACTERS_PATH = 'https://ghibliapi.herokuapp.com/people'

    def find_all(self):
        response = requests.get(MoviesRepository.MOVIE_LIST_PATH)
        if response.ok:
            return list(map(parse_movie, response.json()))
        else:
            return []

    def find_characters(self, movie_id):
        response = requests.get(MoviesRepository.CHARACTERS_PATH, params={
            'film': movie_id
        })

        if response.ok:
            return list(map(parse_character, response.json()))
        else:
            return []
