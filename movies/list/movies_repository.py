import requests
from .movie import Movie


def convertToEntity(jsonMovie):
    return Movie(jsonMovie['id'],
                 jsonMovie['title'],
                 jsonMovie['description'],
                 int(jsonMovie['release_date']))


class MoviesRepository:
    MOVIE_LIST_PATH = 'https://ghibliapi.herokuapp.com/films'

    def find_all(self):
        response = requests.get(MoviesRepository.MOVIE_LIST_PATH)
        if response.ok:
            return map(convertToEntity, response.json())
        else:
            return []
