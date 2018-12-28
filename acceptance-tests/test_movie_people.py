from selenium import webdriver
from django.test import tag
from project.testing import DatabaselessLiveServerTestCase


@tag('acceptance-tests')
class TestMoviePeople(DatabaselessLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_should_show_the_people_in_a_movie(self):
        # if the user goes to the main app url
        self.browser.get(self.live_server_url + '/movies')

        # and clicks on the title of a movie
        first_movie_title = \
            self.browser.find_element_by_class_name('title-link')
        first_movie_title.click()

        # the people that appear in it should be listed
        self.assertEqual(self.browser.title, "Movie characters")
        self.assertIn('/characters', self.browser.current_url)

        characters = self.browser.find_elements_by_class_name('character')
        self.assertGreater(len(characters), 0)

        # each one with its own name and gender
        for character in characters:
            name = character.find_element_by_class_name('name')
            self.assertTrue(name.text.strip())

            gender = character.find_element_by_class_name('gender')
            self.assertIn(gender.text.strip(), ['Male', 'Female', 'NA'])
