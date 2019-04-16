import unittest

from anna_lib.selenium import driver, assertions


class TestUrlEquals(unittest.TestCase):
	def setUp(self):
		self.driver = driver.create(driver='chrome', headless=True)

	def tearDown(self):
		self.driver.close()

	def test_passed(self):
		self.driver.get('http://localhost:8000/test')
		self.assertTrue(assertions.url_equals(self.driver, 'http://localhost:8000/test/', timeout=0))
		self.driver.get('http://localhost:8000/')
		self.assertTrue(assertions.url_equals(self.driver, 'http://localhost:8000/', timeout=0))
		self.driver.get('http://localhost:8000/test/?q=asdf+asdf+asdf')
		self.assertTrue(assertions.url_equals(self.driver, 'http://localhost:8000/test/?q=asdf+asdf+asdf', timeout=0))

	def test_not_passed(self):
		with self.assertRaises(ValueError):
			assertions.url_equals(self.driver, 'annahub.com', timeout=0)
		with self.assertRaises(ValueError):
			assertions.url_equals(self.driver, '/page', timeout=0)
		with self.assertRaises(ValueError):
			assertions.url_equals(self.driver, 'page/', timeout=0)
		with self.assertRaises(ValueError):
			assertions.url_equals(self.driver, '/pag/', timeout=0)
		with self.assertRaises(ValueError):
			assertions.url_equals(self.driver, 'http://localhost:8000/page', timeout=0)
		with self.assertRaises(ValueError):
			assertions.url_equals(self.driver, 'http://localhost:8000/page/', timeout=0)
