import unittest

from anna_lib.selenium import events
from tests.unit.selenium.driver import driver


class TestClick(unittest.TestCase):
	def setUp(self):
		driver.get('http://localhost:8000/test')

	def test_click_element_not_present(self):
		self.assertFalse(events.click(driver=driver, target='#test-click-', timeout=0))

	def test_click(self):
		self.assertFalse(events.wait(driver=driver, target='.clicked', timeout=0))
		events.click(driver=driver, target='#test-click', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='.clicked', timeout=0))

	def test_click_css_selector(self):
		self.assertFalse(events.wait(driver=driver, target='$css.clicked', timeout=0))
		events.click(driver=driver, target='$css#test-click', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='$css.clicked', timeout=0))

	def test_click_xpath_selector(self):
		self.assertFalse(events.wait(driver=driver, target='$xpath//body/button[@class="clicked"]', timeout=0))
		events.click(driver=driver, target='$xpath//body/button[@id="test-click"]', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='$xpath//body/button[@class="clicked"]', timeout=0))
