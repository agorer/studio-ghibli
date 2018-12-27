from django.test import SimpleTestCase
from django.urls import resolve
from movies.characters.views import characters_page
from unittest import mock
from .character import Character


class TestCharacterView(SimpleTestCase):
    def setUp(self):
        self.list_of_movie_characters = [
            Character('character-id-1', 'Ashitaka', 'Male'),
            Character('character-id-2', 'San', 'Female')
        ]

    def test_should_go_to_the_correct_view(self):
        found_page = resolve('/movies/1/characters')

        self.assertEqual(found_page.func, characters_page)

    def test_uses_characters_template(self):
        response = self.client.get('/movies/1/characters')

        self.assertTemplateUsed(response, 'movies/characters/characters.html')

    @mock.patch('movies.characters.views.MoviesRepository')
    def test_should_return_characters_from_repository(self, repository):
        repository.return_value.find_characters.return_value = \
            self.list_of_movie_characters

        response = self.client.get('/movies/1/characters')

        self.assertEquals(response.status_code, 200)
        self.assertCountEqual(response.context['characters'],
                              self.list_of_movie_characters)
