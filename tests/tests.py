import unittest
from snowy import retrieve_news, parse_news

class SnowyTest(unittest.TestCase):

	def test_retrieve_news(self):
		self.assertEqual(retrieve_news().status_code, 200)

	def test_parse_news(self):
		self.assertIsNotNone(parse_news(retrieve_news()))

	# def test_retrieve_movies(self):
	# 	pass

	# def test_retrieve_word_day(self):
	# 	pass

if __name__ == '__main__':
	unittest.main()