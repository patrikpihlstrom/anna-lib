import unittest

from anna_lib.selenium import assertions
from tests.unit.selenium.driver import driver


class ElementExists(unittest.TestCase):
	def setUp(self):
		driver.get('http://localhost:8000/test')

	def test_passed(self):
		self.assertTrue(assertions.element_exists(driver, '#test-click', timeout=0))
		self.assertTrue(assertions.element_exists(driver, '$css#test-click', timeout=0))
		self.assertTrue(assertions.element_exists(driver, '$xpath//select[@name="xpath"]/option[@value="option"]', timeout=0))
		self.assertTrue(assertions.element_exists(driver, '.get-list', timeout=0))
		self.assertTrue(assertions.element_exists(driver, '$css.get-list', timeout=0))
		self.assertTrue(assertions.element_exists(driver, 'a[href="http://localhost:8000/test/switchto"]', timeout=0))
		self.assertTrue(assertions.element_exists(driver, '$cssa[href="http://localhost:8000/test/switchto"]', timeout=0))

	def test_not_passed(self):
		with self.assertRaises(TypeError):
			assertions.element_exists(driver, '#test-click-', timeout=0)
		with self.assertRaises(TypeError):
			assertions.element_exists(driver, '$css#test-click-', timeout=0)
		with self.assertRaises(TypeError):
			assertions.element_exists(driver, '$xpath//select[@name="xpath"]/option[@value="not option"]', timeout=0)
		with self.assertRaises(TypeError):
			assertions.element_exists(driver, '.get-lists', timeout=0)
		with self.assertRaises(TypeError):
			assertions.element_exists(driver, '$css.get-lists', timeout=0)
		with self.assertRaises(TypeError):
			assertions.element_exists(driver, 'a[href^="https://"]', timeout=0)
		with self.assertRaises(TypeError):
			assertions.element_exists(driver, '$cssa[href^="https://"]', timeout=0)
