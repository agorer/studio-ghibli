from selenium import webdriver
import unittest


class MovieListTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_should_contain_a_list_of_movies(self):
        # if the user goes to the main app url
        self.browser.get('http://localhost:8000/movies')

        # she should be able to see a plain list of all movies Studio Ghibli
        # movies
        movies = self.browser.find_elements_by_class_name('movie')
        self.assertGreater(len(movies), 10)

        # each one with its own title, description and release date
        for movie in movies:
            title = movie.find_element_by_class_name('title')
            self.assertTrue(title.text.strip())

            description = movie.find_element_by_class_name('description')
            self.assertTrue(description.text.strip())

            release_date = movie.find_element_by_class_name('release-date')
            self.assertTrue(release_date.text.strip().isdigit())


if __name__ == '__main__':
    unittest.main()
