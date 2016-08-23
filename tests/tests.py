import unittest
import config

from snowy import retrieve_news, send_news
from snowy import retrieve_movies, send_movies

class SnowyTest(unittest.TestCase):

	def test_retrieve_news(self):
		self.assertEqual(retrieve_news(config.news['SOURCE'], 
				config.news['KEY']).status_code, 200)

	def test_news_return(self):
		self.assertIsNotNone(send_news)

	def test_retrieve_movies(self):
		self.assertEqual(retrieve_movies(
			config.movies['SOURCE']).status_code, 200)

	def test_movies_return(self):
		self.assertIsNotNone(send_movies)

if __name__ == '__main__':
	unittest.main()