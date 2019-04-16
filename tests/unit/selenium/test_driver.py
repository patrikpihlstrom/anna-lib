import unittest

from selenium.common.exceptions import WebDriverException

from anna_lib.selenium.driver import create


class TestDriver(unittest.TestCase):
	def setUp(self):
		self.driver = None

	def tearDown(self):
		if self.driver is not None:
			try:
				self.driver.close()
			except WebDriverException:
				pass

	def test_create_no_driver(self):
		self.driver = create(headless=True)
		self.assertEqual(self.driver.name, 'firefox')
		self.driver.close()

	def test_create_invalid_driver(self):
		with self.assertRaises(TypeError):
			self.driver = create(driver='ie', headless=True)
		with self.assertRaises(TypeError):
			self.driver = create(driver='edge', headless=True)
		with self.assertRaises(TypeError):
			self.driver = create(driver='opera', headless=True)
		with self.assertRaises(TypeError):
			self.driver = create(driver='safari', headless=True)

	def test_create_driver_chrome(self):
		self.driver = create(driver='chrome', headless=True)
		self.assertEqual(self.driver.name, 'chrome')
		res = tuple(self.driver.get_window_size('current').values())
		self.assertEqual((1920, 1080), res)
		self.driver.close()

	def test_create_driver_firefox(self):
		self.driver = create(driver='firefox', headless=True)
		self.assertEqual(self.driver.name, 'firefox')
		res = tuple(self.driver.get_window_size('current').values())
		self.assertEqual((1920, 1080), res)
		self.driver.close()

	def test_create_resolution(self):
		self.driver = create(driver='chrome', headless=True, resolution=(1024, 1024))
		self.assertEqual(self.driver.name, 'chrome')
		res = tuple(self.driver.get_window_size('current').values())
		self.assertEqual((1024, 1024), res)
		self.driver.close()

	def test_create_invalid_resolution(self):
		with self.assertRaises(TypeError):
			create(driver='chrome', headless=True, resolution=(1024,))
		with self.assertRaises(TypeError):
			create(driver='chrome', headless=True, resolution=(-1024, 1024))
		with self.assertRaises(TypeError):
			create(driver='chrome', headless=True, resolution=(None,))
		with self.assertRaises(TypeError):
			create(driver='chrome', headless=True, resolution=('foo', 'bar'))
