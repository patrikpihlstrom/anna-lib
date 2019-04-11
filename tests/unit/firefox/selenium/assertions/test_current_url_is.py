import unittest

from anna_lib.selenium import driver, assertions


class TestCurrentUrlIs(unittest.TestCase):
	def setUp(self):
		self.driver = driver.create(driver='firefox', headless=True)

	def tearDown(self):
		self.driver.close()

	def test_passed(self):
		self.driver.get('http://localhost:8000/test')
		self.assertTrue(assertions.current_url_is(self.driver, 'http://localhost:8000/test/', timeout=0)['passed'])
		self.driver.get('http://localhost:8000/')
		self.assertTrue(assertions.current_url_is(self.driver, 'http://localhost:8000/', timeout=0)['passed'])
		self.driver.get('http://localhost:8000/test/?q=asdf+asdf+asdf')
		self.assertTrue(assertions.current_url_is(self.driver, 'http://localhost:8000/test/?q=asdf+asdf+asdf', timeout=0)['passed'])

	def test_not_passed(self):
		self.assertFalse(assertions.current_url_is(self.driver, 'annahub.com', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_is(self.driver, '/page', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_is(self.driver, 'page/', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_is(self.driver, '/pag/', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_is(self.driver, 'http://localhost:8000/page', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_is(self.driver, 'http://localhost:8000/page/', timeout=0)['passed'])
