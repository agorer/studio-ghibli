from django.test import SimpleTestCase, tag
from .movie import Movie
from movies.characters.character import Character
from .movies_cache import (cache_movies,
                           get_cached_movies,
                           movies_are_cached,
                           cache_characters,
                           get_cached_characters,
                           characters_are_cached)
import time
from django.core.cache import cache


@tag('integration-tests')
class TestMoviesCache(SimpleTestCase):
    '''
        [IMPORTANT] These test should not be run in parallel because the all
        use the same cache.
    '''

    def setUp(self):
        cache.clear()

        self.movies = [
            Movie('movie-id-1', 'Movie Title', 'Long Description', 1981),
            Movie('movie-id-2', 'Movie Title 2', 'Long Description 2', 1982)
        ]

        self.characters = [
            Character('character-id-1', 'Character Name', 'Male'),
            Character('character-id-2', 'Character Name 2', 'Female')
        ]

    def test_should_find_recently_cached_movies(self):
        cache_movies(self.movies)
        cached_movies = get_cached_movies()

        self.assertEqual(len(self.movies), len(cached_movies))
        for movie, cached_movie in zip(self.movies, cached_movies):
            self.assertEqual(movie.id, cached_movie.id)

    def test_should_know_if_movies_are_cached(self):
        cache_movies(self.movies)
        self.assertTrue(movies_are_cached())

    def test_should_know_if_movies_are_not_cached(self):
        self.assertFalse(movies_are_cached())

    def test_should_find_recently_cached_characters(self):
        cache_characters('movie-id', self.characters)
        cached_characters = get_cached_characters('movie-id')

        self.assertEqual(len(self.characters), len(cached_characters))
        for character, cached_character in zip(self.characters,
                                               cached_characters):
            self.assertEqual(character.id, cached_character.id)

    def test_should_know_if_characters_are_cached(self):
        cache_characters('movie-id', self.characters)
        self.assertTrue(characters_are_cached('movie-id'))

    def test_should_know_if_characters_are_not_cached(self):
        self.assertFalse(characters_are_cached('movie-id'))

    # Test speed could be improved by making cache timeout configurable
    def test_should_cache_for_only_60_seconds(self):
        cache_movies(self.movies)
        time.sleep(61)

        self.assertEqual(get_cached_movies(), None)
