from django.test import SimpleTestCase
from django.urls import resolve
from movies.list.views import movie_list_page
from unittest import mock
from .movie import Movie


class TestListView(SimpleTestCase):
    def setUp(self):
        self.list_of_2_movies = [
            Movie('movie-id-1', 'Movie Title', 'Long Description', 1981),
            Movie('movie-id-2', 'Movie Title 2', 'Long Description 2', 1982)
        ]

    def test_should_go_to_the_correct_view(self):
        found_page = resolve('/movies')

        self.assertEqual(found_page.func, movie_list_page)

    def test_uses_movies_template(self):
        response = self.client.get('/movies')

        self.assertTemplateUsed(response, 'movies/list/movie_list.html')

    @mock.patch('movies.list.views.MoviesRepository')
    def test_returns_movies_from_repository(self, repository):
        repository.return_value.find_all.return_value = self.list_of_2_movies

        response = self.client.get('/movies')

        self.assertEquals(response.status_code, 200)
        self.assertCountEqual(response.context['movies'],
                              self.list_of_2_movies)
