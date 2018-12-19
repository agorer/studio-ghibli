from django.test import SimpleTestCase
from django.urls import resolve
from movies.list.views import movie_list_page


class TestListView(SimpleTestCase):
    def test_should_go_to_the_correct_view(self):
        found_page = resolve('/')
        self.assertEqual(found_page.func, movie_list_page)
