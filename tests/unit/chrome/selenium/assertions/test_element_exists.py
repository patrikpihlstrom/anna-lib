import unittest

from anna_lib.selenium import driver, assertions


class ElementExists(unittest.TestCase):
	def setUp(self):
		self.driver = driver.create(driver='chrome', headless=True)
		self.driver.get('http://localhost:8000/test')

	def tearDown(self):
		self.driver.close()

	def test_passed(self):
		self.assertTrue(assertions.element_exists(self.driver, '#test-click', timeout=0)['passed'])
		self.assertTrue(assertions.element_exists(self.driver, '$css#test-click', timeout=0)['passed'])
		self.assertTrue(assertions.element_exists(self.driver, '$xpath//select[@name="xpath"]/option[@value="option"]', timeout=0)['passed'])
		self.assertTrue(assertions.element_exists(self.driver, '.get-list', timeout=0)['passed'])
		self.assertTrue(assertions.element_exists(self.driver, '$css.get-list', timeout=0)['passed'])
		self.assertTrue(assertions.element_exists(self.driver, 'a[href="http://localhost:8000/test/switchto"]', timeout=0)['passed'])
		self.assertTrue(assertions.element_exists(self.driver, '$cssa[href="http://localhost:8000/test/switchto"]', timeout=0)['passed'])

	def test_not_passed(self):
		self.assertFalse(assertions.element_exists(self.driver, '#test-click-', timeout=0)['passed'])
		self.assertFalse(assertions.element_exists(self.driver, '$css#test-click-', timeout=0)['passed'])
		self.assertFalse(assertions.element_exists(self.driver, '$xpath//select[@name="xpath"]/option[@value="not option"]', timeout=0)['passed'])
		self.assertFalse(assertions.element_exists(self.driver, '.get-lists', timeout=0)['passed'])
		self.assertFalse(assertions.element_exists(self.driver, '$css.get-lists', timeout=0)['passed'])
		self.assertFalse(assertions.element_exists(self.driver, 'a[href^="https://"]', timeout=0)['passed'])
		self.assertFalse(assertions.element_exists(self.driver, '$cssa[href^="https://"]', timeout=0)['passed'])
