import unittest
import config

from snowy import retrieve_news, news_ret_val
from snowy import retrieve_movies, movie_ret_val

class SnowyTest(unittest.TestCase):

	def test_retrieve_news(self):
		self.assertEqual(retrieve_news(config.news['SOURCE'], 
				config.news['KEY']).status_code, 200)

	def test_news_return(self):
		self.assertIsNotNone(news_ret_val)

	def test_retrieve_movies(self):
		self.assertEqual(retrieve_movies(
			config.movies['SOURCE']).status_code, 200)

	def test_movies_return(self):
		self.assertIsNotNone(movie_ret_val)

if __name__ == '__main__':
	unittest.main()