import unittest

from anna_lib.selenium import assertions
from tests.unit.selenium.driver import driver


class TestInUrl(unittest.TestCase):
	def setUp(self):
		driver.get('http://localhost:8000/test')

	def test_passed(self):
		self.assertTrue(assertions.in_url(driver, 'localhost', timeout=0))
		self.assertTrue(assertions.in_url(driver, '/test', timeout=0))
		self.assertTrue(assertions.in_url(driver, 'test/', timeout=0))
		self.assertTrue(assertions.in_url(driver, '/test/', timeout=0))
		self.assertTrue(assertions.in_url(driver, 'http://localhost:8000/test', timeout=0))
		self.assertTrue(assertions.in_url(driver, 'http://localhost:8000/test/', timeout=0))

	def test_not_passed(self):
		self.assertFalse(assertions.in_url(driver, 'annahub.com', timeout=0))
		self.assertFalse(assertions.in_url(driver, '/page', timeout=0))
		self.assertFalse(assertions.in_url(driver, 'page/', timeout=0))
		self.assertFalse(assertions.in_url(driver, '/pag/', timeout=0))
		self.assertFalse(assertions.in_url(driver, 'http://localhost:8000/page', timeout=0))
		self.assertFalse(assertions.in_url(driver, 'http://localhost:8000/page/', timeout=0))
