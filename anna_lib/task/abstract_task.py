import abc

from selenium.webdriver.remote.webdriver import WebDriver

from anna_lib.selenium import assertions


class AbstractTask(object):
	driver: WebDriver

	def __init__(self, driver):
		self.driver = driver
		self.result = []
		self.passed = False
		self.required = True

	def execute(self) -> None:
		self.before_execute()
		self.__execute__()
		self.after_execute()
		if self.required:
			self.passed = not any(not r['passed'] for r in self.result)
		else:
			self.passed = True

	@abc.abstractmethod
	def before_execute(self) -> None:
		pass

	@abc.abstractmethod
	def __execute__(self) -> None:
		pass

	@abc.abstractmethod
	def after_execute(self) -> None:
		pass

	def assert_element_exists(self, target: str) -> None:
		self.result.append(
			{
				'assertion': 'element_exists',
				'passed': assertions.element_exists(driver=self.driver, target=target)
			})

	def assert_url_equals(self, expected: str) -> None:
		self.result.append(
			{
				'assertion': 'in_url',
				'passed': assertions.url_equals(driver=self.driver, expected=expected),
				'expected': expected,
				'url': self.driver.current_url
			})

	def assert_in_url(self, part: str) -> None:
		self.result.append(
			{
				'assertion': 'in_url',
				'passed': assertions.in_url(driver=self.driver, part=part),
				'part': part,
				'url': self.driver.current_url
			})
