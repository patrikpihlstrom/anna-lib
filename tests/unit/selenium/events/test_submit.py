import unittest

from anna_lib.selenium import events
from tests.unit.selenium.driver import driver


class TestSubmit(unittest.TestCase):
	def setUp(self):
		driver.get('http://localhost:8000/test')

	def test_submit_element_not_present(self):
		self.assertFalse(events.submit(driver=driver, target='#test-submit-', timeout=0))

	def test_submit_element_present(self):
		self.assertFalse(events.wait(driver=driver, target='.submitted', timeout=0))
		events.submit(driver=driver, target='#test-submit', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='.submitted', timeout=0))

	def test_submit_not_submittable(self):
		self.assertFalse(events.submit(driver=driver, target='.get-list', timeout=0))

	def test_submit_css_selector(self):
		self.assertFalse(events.wait(driver=driver, target='$css.submitted', timeout=0))
		events.submit(driver=driver, target='$css#test-submit', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='$css.submitted', timeout=0))

	def test_submit_xpath_selector(self):
		self.assertFalse(events.wait(driver=driver, target='$xpath//body/form[@class="submitted"]', timeout=0))
		events.submit(driver=driver, target='$xpath//body/form[@id="test-submit"]', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='$xpath//body/form[@class="submitted"]', timeout=0))
