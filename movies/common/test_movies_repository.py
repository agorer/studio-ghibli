from django.test import SimpleTestCase
from .movies_repository import MoviesRepository
from .movie import Movie
from movies.characters.character import Character
from unittest import mock


class TestMoviesRepository(SimpleTestCase):
    def setUp(self):
        self.repository = MoviesRepository()

        self.movies = [
            Movie('movie-id-1', 'Movie Title', 'Long Description', 1981),
            Movie('movie-id-2', 'Movie Title 2', 'Long Description 2', 1982)
        ]

        self.characters = [
            Character('character-id-1', 'Character Name', 'Male'),
            Character('character-id-2', 'Character Name 2', 'Female')
        ]

    @mock.patch('movies.common.movies_repository.movies_cache')
    def test_should_return_cached_data_movies_if_exists(self,
                                                        movies_cache):
        movies_cache.movies_are_cached.return_value = True
        movies_cache.get_cached_movies.return_value = self.movies

        movies = self.repository.find_all()

        self.assertCountEqual(movies, self.movies)

    @mock.patch('movies.common.movies_repository.movies_cache')
    @mock.patch('movies.common.movies_repository.api_client')
    def test_should_return_movies_api_data_if_not_cached(self, api_client,
                                                         movies_cache):
        movies_cache.movies_are_cached.return_value = False
        api_client.find_movies.return_value = self.movies

        movies = self.repository.find_all()

        self.assertCountEqual(movies, self.movies)
        movies_cache.cache_movies.assert_called_once()

    @mock.patch('movies.common.movies_repository.movies_cache')
    def test_should_return_cached_data_characters_if_exists(self,
                                                            movies_cache):
        movies_cache.characters_are_cached.return_value = True
        movies_cache.get_cached_characters.return_value = self.characters

        characters = self.repository.find_characters('movie-id')

        self.assertCountEqual(characters, self.characters)

    @mock.patch('movies.common.movies_repository.movies_cache')
    @mock.patch('movies.common.movies_repository.api_client')
    def test_should_return_characters_api_data_if_not_cached(self, api_client,
                                                             movies_cache):
        movies_cache.characters_are_cached.return_value = False
        api_client.find_characters.return_value = self.characters

        characters = self.repository.find_characters('movie-id')

        self.assertCountEqual(characters, self.characters)
        movies_cache.cache_characters.assert_called_once()
