import unittest

from anna_lib.selenium import driver, assertions


class TestCurrentUrlIn(unittest.TestCase):
	def setUp(self):
		self.driver = driver.create({'driver': 'chrome', 'headless': True})
		self.driver.get('http://annahub.se:8000/test')

	def tearDown(self):
		self.driver.close()

	def test_passed(self):
		self.assertTrue(assertions.current_url_in(self.driver, 'annahub.se', timeout=0)['passed'])
		self.assertTrue(assertions.current_url_in(self.driver, '/test', timeout=0)['passed'])
		self.assertTrue(assertions.current_url_in(self.driver, 'test/', timeout=0)['passed'])
		self.assertTrue(assertions.current_url_in(self.driver, '/test/', timeout=0)['passed'])
		self.assertTrue(assertions.current_url_in(self.driver, 'http://annahub.se:8000/test', timeout=0)['passed'])
		self.assertTrue(assertions.current_url_in(self.driver, 'http://annahub.se:8000/test/', timeout=0)['passed'])

	def test_not_passed(self):
		self.assertFalse(assertions.current_url_in(self.driver, 'annahub.com', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_in(self.driver, '/page', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_in(self.driver, 'page/', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_in(self.driver, '/pag/', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_in(self.driver, 'http://annahub.se:8000/page', timeout=0)['passed'])
		self.assertFalse(assertions.current_url_in(self.driver, 'http://annahub.se:8000/page/', timeout=0)['passed'])
