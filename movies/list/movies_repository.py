import requests
from .api_movie_parser import parse


class MoviesRepository:
    MOVIE_LIST_PATH = 'https://ghibliapi.herokuapp.com/films'

    def find_all(self):
        response = requests.get(MoviesRepository.MOVIE_LIST_PATH)
        if response.ok:
            return map(parse, response.json())
        else:
            return []
