import unittest

from anna_lib.selenium import driver, util
from selenium.webdriver.remote.webelement import WebElement
from tests.unit.selenium.driver import driver


class TestUtil(unittest.TestCase):
	def setUp(self):
		driver.get('http://localhost:8000/test')

	def test_get_element_css_id(self):
		element = util.get_element(driver, '#test-send-keys')
		self.assertIsInstance(element, WebElement)

	def test_get_element_css_class(self):
		element = util.get_element_css(driver, '.get-list')
		self.assertIsInstance(element, WebElement)

	def test_get_element_css_attribute(self):
		element = util.get_element_css(driver, 'a[href^="http"')
		self.assertIsInstance(element, WebElement)

	def test_get_elements_css(self):
		elements = util.get_element_css(driver, '.get-list', False)
		self.assertIsInstance(elements, list)
		self.assertIsInstance(elements[0], WebElement)

	def test_get_element_xpath(self):
		element = util.get_element_xpath(driver, '//select[@name="xpath"]/option[@value="option"]')
		self.assertIsInstance(element, WebElement)

	def test_get_elements_xpath(self):
		elements = util.get_element_xpath(driver, '//select[@name="xpath"]/option', False)
		self.assertIsInstance(elements, list)
		self.assertIsInstance(elements[0], WebElement)
