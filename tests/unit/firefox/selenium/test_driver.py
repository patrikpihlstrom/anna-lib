import unittest

from anna_lib.selenium import driver


class TestEvents(unittest.TestCase):
	def setUp(self):
		self.driver = None

	def tearDown(self):
		if self.driver is not None:
			self.driver.close()

	def test_create_no_driver(self):
		with self.assertRaises(KeyError):
			self.driver = driver.create({'headless': True})

	def test_create_invalid_driver(self):
		with self.assertRaises(TypeError):
			self.driver = driver.create({'headless': True, 'driver': 'ie'})
		with self.assertRaises(TypeError):
			self.driver = driver.create({'headless': True, 'driver': 'edge'})
		with self.assertRaises(TypeError):
			self.driver = driver.create({'headless': True, 'driver': 'opera'})
		with self.assertRaises(TypeError):
			self.driver = driver.create({'headless': True, 'driver': 'safari'})

	def test_create_driver(self):
		self.driver = driver.create({'headless': True, 'driver': 'firefox'})
		self.assertEqual(self.driver.name, 'firefox')
		res = tuple(self.driver.get_window_size(self.driver.current_window_handle).values())
		self.assertEqual((1920, 1080), res)

	def test_create_resolution(self):
		self.driver = driver.create({'headless': True, 'driver': 'firefox', 'resolution': '1024x1024'})
		self.assertEqual(self.driver.name, 'firefox')
		res = tuple(self.driver.get_window_size(self.driver.current_window_handle).values())
		self.assertEqual((1024, 1024), res)
