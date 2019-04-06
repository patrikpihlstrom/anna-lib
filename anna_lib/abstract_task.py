import abc


class AbstractTask(object):
	result = []

	def __init__(self, driver):
		self.driver = driver

	@abc.abstractmethod
	def before_execute(self):
		pass

	@abc.abstractmethod
	def execute(self):
		pass

	@abc.abstractmethod
	def after_execute(self):
		pass
