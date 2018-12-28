from .api_client import find_movies, find_characters


class MoviesRepository:
    def find_all(self):
        return find_movies()

    def find_characters(self, movie_id):
        return find_characters(movie_id)
