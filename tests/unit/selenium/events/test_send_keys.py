import unittest

from anna_lib.selenium import events
from tests.unit.selenium.driver import driver


class TestSendKeys(unittest.TestCase):
	def setUp(self):
		driver.get('http://localhost:8000/test')

	def test_send_keys_element_not_present(self):
		self.assertFalse(events.send_keys(driver=driver, target='#test-send-keys-', value='test_send_keys', timeout=0))

	def test_send_keys_input_text(self):
		self.assertFalse(events.wait(driver=driver, target='.test_send_keys', timeout=0))
		events.send_keys(driver=driver, target='#test-send-keys', value='test_send_keys', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='.test_send_keys', timeout=0))

	def test_send_keys_textarea(self):
		self.assertFalse(events.wait(driver=driver, target='.test_send_keys_textarea', timeout=0))
		events.send_keys(driver=driver, target='#test-send-keys-textarea', value='test_send_keys_textarea', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='.test_send_keys_textarea', timeout=0))

	def test_send_keys_css_selector(self):
		self.assertFalse(events.wait(driver=driver, target='$css.test_send_keys', timeout=0))
		events.send_keys(driver=driver, target='$css#test-send-keys', value='test_send_keys', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='$css.test_send_keys', timeout=0))

	def test_send_keys_xpath_selector(self):
		self.assertFalse(events.wait(driver=driver, target='$xpath//body/input[@class="test_send_keys"]', timeout=0))
		events.send_keys(driver=driver, target='$xpath//body/input[@id="test-send-keys"]', value='test_send_keys', timeout=0)
		self.assertTrue(events.wait(driver=driver, target='$xpath//body/input[@class="test_send_keys"]', timeout=0))
