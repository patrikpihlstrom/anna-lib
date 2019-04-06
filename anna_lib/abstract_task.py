import abc


class AbstractTask(object):
	def __init__(self, driver):
		self.driver = driver
		self.result = []
		self.passed = False
		self.required = True

	@abc.abstractmethod
	def before_execute(self):
		pass

	@abc.abstractmethod
	def execute(self):
		pass

	@abc.abstractmethod
	def after_execute(self):
		if self.required:
			self.passed = not any(not r['passed'] for r in self.result)
		else:
			self.passed = True
