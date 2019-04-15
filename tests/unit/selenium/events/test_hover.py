import unittest

from anna_lib.selenium import events
from tests.unit.selenium.driver import driver


class TestHover(unittest.TestCase):
	def setUp(self):
		driver.get('http://localhost:8000/test')

	def test_hover_element_not_present(self):
		self.assertFalse(events.hover(driver=driver, target='#test-hover-', timeout=0))

	def test_hover_element_present(self):
		self.assertFalse(events.wait(driver=driver, target='.hovered', timeout=0))
		events.hover(driver=driver, target='#test-hover', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='.hovered', timeout=0))

	def test_hover_css_selector(self):
		self.assertFalse(events.wait(driver=driver, target='$css.hovered', timeout=0))
		events.hover(driver=driver, target='$css#test-hover', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='$css.hovered', timeout=0))

	def test_hover_xpath_selector(self):
		self.assertFalse(events.wait(driver=driver, target='$xpath//body/button[@class="hovered"]', timeout=0))
		events.hover(driver=driver, target='$xpath//body/button[@id="test-hover"]', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='$xpath//body/button[@class="hovered"]', timeout=0))
