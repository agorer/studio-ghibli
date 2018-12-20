from django.test import SimpleTestCase
from .movies_repository import MoviesRepository


class TestMoviesRepository(SimpleTestCase):
    def setUp(self):
        self.repository = MoviesRepository()

    def test_should_find_all_movies(self):
        movies = self.repository.find_all()

        for movie in movies:
            self.assertTrue(len(movie.id))
            self.assertTrue(len(movie.title))
            self.assertTrue(len(movie.description))
            self.assertTrue(type(movie.release_date) is int)
