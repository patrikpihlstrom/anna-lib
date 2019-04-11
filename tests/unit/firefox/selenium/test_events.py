import unittest

from anna_lib.selenium import driver
from anna_common.task import factory as task_factory


class TestEvents(unittest.TestCase):
	def setUp(self):
		self.driver = driver.create({'driver': 'firefox', 'headless': True})
		self.driver.get('http://annahub.se:8000/test')

	def tearDown(self):
		self.driver.close()

	def test_send_keys(self):
		name, task = task_factory.create(self.driver, 'test', 'send_keys')
		task.execute()
		self.assertTrue(task.passed)

	def test_submit(self):
		name, task = task_factory.create(self.driver, 'test', 'submit')
		task.execute()
		self.assertTrue(task.passed)

	def test_click(self):
		name, task = task_factory.create(self.driver, 'test', 'click')
		task.execute()
		self.assertTrue(task.passed)

	def test_hover(self):
		name, task = task_factory.create(self.driver, 'test', 'hover')
		task.execute()
		self.assertTrue(task.passed)

	def test_wait(self):
		name, task = task_factory.create(self.driver, 'test', 'wait')
		task.execute()
		self.assertTrue(task.passed)

	def test_switch_to(self):
		name, task = task_factory.create(self.driver, 'test', 'switch_to')
		task.execute()
		self.assertTrue(task.passed)

	def test_fail(self):
		name, task = task_factory.create(self.driver, 'test', 'fail')
		task.execute()
		self.assertFalse(task.passed)
