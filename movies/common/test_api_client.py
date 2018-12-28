from django.test import SimpleTestCase
from .api_client import find_movies, find_characters
from unittest import mock


class TestApiClient(SimpleTestCase):

    def test_should_find_all_movies(self):
        movies = find_movies()

        for movie in movies:
            self.assertTrue(len(movie.id))
            self.assertTrue(len(movie.title))
            self.assertTrue(len(movie.description))
            self.assertTrue(type(movie.release_date) is int)

    @mock.patch('requests.get')
    def test_should_return_empty_list_of_movies_when_api_errors(self, get):
        get.return_value.json.return_value = 'Error message'
        get.return_value.ok = False

        movies = find_movies()

        self.assertEqual(movies, [])

    def test_should_find_all_characters_of_a_movie(self):
        movie_id = find_movies()[0].id

        characters = find_characters(movie_id)

        for character in characters:
            self.assertTrue(len(character.id))
            self.assertTrue(len(character.name))
            self.assertIn(character.gender, ['Male', 'Female', 'NA'])

    @mock.patch('requests.get')
    def test_should_return_empty_list_of_characters_when_api_errors(self, get):
        get.return_value.json.return_value = 'Error message'
        get.return_value.ok = False

        characters = find_characters('a-film-id')

        self.assertEqual(characters, [])
