from . import api_client
from . import movies_cache


class MoviesRepository:
    def find_all(self):
        if movies_cache.movies_are_cached():
            return movies_cache.get_cached_movies()
        else:
            api_movies = api_client.find_movies()
            movies_cache.cache_movies(api_movies)
            return api_movies

    def find_characters(self, movie_id):
        if movies_cache.characters_are_cached(movie_id):
            return movies_cache.get_cached_characters(movie_id)
        else:
            api_characters = api_client.find_characters(movie_id)
            movies_cache.cache_characters(movie_id, api_characters)
            return api_characters
