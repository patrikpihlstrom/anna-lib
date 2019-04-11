import time
from selenium.common.exceptions import NoSuchElementException


def get_element(driver, target, get_first=True, timeout=16):
	"""
	Default behavior is to return the first element that matches the target
	:param type:
	:param driver:
	:param target:
	:param get_first:
	:param timeout:
	:return:
	"""

	if target.startswith('$xpath'):
		return get_element_xpath(driver, target[6:], get_first, timeout)
	elif target.startswith('$css'):
		return get_element_css(driver, target[4:], get_first, timeout)
	return get_element_css(driver, target, get_first, timeout)


def get_element_css(driver, target, get_first=True, timeout=16):
	try:
		if get_first:
			return driver.find_element_by_css_selector(target)
		else:
			return driver.find_elements_by_css_selector(target)
	except (TimeoutError, NoSuchElementException) as e:
		if timeout <= 0:
			return False, e
		time.sleep(1)
		return get_element(driver, target, get_first, timeout - 1)


def get_element_xpath(driver, target, get_first=True, timeout=16):
	try:
		if get_first:
			return driver.find_element_by_xpath(target)
		else:
			return driver.find_elements_by_xpath(target)
	except (TimeoutError, NoSuchElementException) as e:
		if timeout <= 0:
			return False, e
		time.sleep(1)
		return get_element(driver, '$xpath' + target, get_first, timeout - 1)


def get_text(driver, target):
	element = get_element(driver, target, True)
	return element.text
