from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from . import util


def send_keys(driver, target, value):
	if wait(driver, target):
		element = util.get_element(driver=driver, target=target)
		element.send_keys(value.encode('ascii', 'ignore').decode("utf-8"))


def submit(driver, target):
	if wait(driver, target):
		element = util.get_element(driver=driver, target=target)
		element.submit()


def click(driver, target):
	if wait(driver, target):
		element = util.get_element(driver=driver, target=target)
		if element not in (None, False) and element.tag_name == 'option':
			element.click()
		else:
			action = ActionChains(driver)
			action.move_to_element(element)
			action.click(element)
			action.perform()


def hover(driver, target):
	if wait(driver, target):
		element = util.get_element(driver=driver, target=target)
		action = ActionChains(driver)
		action.move_to_element(element)
		action.perform()


def wait(driver, target, clickable=False, required=True):
	"""
	Wait for an element to appear
	:param clickable:
	:param target:
	:param required:
	:param driver:
	:return:
	"""
	try:
		if clickable:
			if target.startswith('$css'):
				WebDriverWait(driver, 16).until(ec.element_to_be_clickable((By.CSS_SELECTOR, target[4:])))
			elif target.startswith('$xpath'):
				WebDriverWait(driver, 16).until(ec.element_to_be_clickable((By.XPATH, target[6:])))
		else:
			if target.startswith('$css'):
				WebDriverWait(driver, 16).until(ec.presence_of_element_located((By.CSS_SELECTOR, target[4:])))
			elif target.startswith('$xpath'):
				WebDriverWait(driver, 16).until(ec.presence_of_element_located((By.XPATH, target[6:])))
	except TimeoutException as e:
		if not required:
			return False
		else:
			raise e
	return True


def switch_to(driver, target):
	scroll_to(driver, target)
	element = util.get_element(driver=driver, target=target)
	driver.switch_to.frame(element)


def scroll_to(driver, target):
	driver.execute_script('arguments[0].scrollIntoView(true);', util.get_element(driver=driver, target=target))
