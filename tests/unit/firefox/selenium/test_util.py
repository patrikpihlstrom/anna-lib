import unittest

from selenium.webdriver.firefox.webelement import FirefoxWebElement

from anna_lib.selenium import driver, util


class TestUtil(unittest.TestCase):
	def setUp(self):
		self.driver = driver.create({'driver': 'firefox', 'headless': True})
		self.driver.get('http://annahub.se:8000/test')

	def tearDown(self):
		self.driver.close()

	def test_get_element_css_id(self):
		element = util.get_element(self.driver, '#test-send-keys')
		self.assertIsInstance(element, FirefoxWebElement)

	def test_get_element_css_class(self):
		element = util.get_element_css(self.driver, '.get-list')
		self.assertIsInstance(element, FirefoxWebElement)

	def test_get_element_css_attribute(self):
		element = util.get_element_css(self.driver, 'a[href^="http"')
		self.assertIsInstance(element, FirefoxWebElement)

	def test_get_elements_css(self):
		elements = util.get_element_css(self.driver, '.get-list', False)
		self.assertIsInstance(elements, list)
		self.assertIsInstance(elements[0], FirefoxWebElement)

	def test_get_element_xpath(self):
		element = util.get_element_xpath(self.driver, '//select[@name="xpath"]/option[@value="option"]')
		self.assertIsInstance(element, FirefoxWebElement)

	def test_get_elements_xpath(self):
		elements = util.get_element_xpath(self.driver, '//select[@name="xpath"]/option', False)
		self.assertIsInstance(elements, list)
		self.assertIsInstance(elements[0], FirefoxWebElement)
