from . import util
import time


def in_url(driver: object, part: str, timeout: int = 16) -> bool:
	passed = part in driver.current_url
	if not passed and timeout > 0:
		time.sleep(1)
		return in_url(driver, part, timeout - 1)
	return passed


def url_equals(driver: object, expected: str, timeout: int = 16) -> bool:
	passed = driver.current_url == expected
	if not passed and timeout > 0:
		time.sleep(1)
		return url_equals(driver, expected, timeout - 1)
	return passed


def element_exists(driver: object, target: str, timeout: int = 16) -> bool:
	element = util.get_element(driver=driver, target=target, timeout=timeout)
	return hasattr(element, 'id') or (isinstance(element, list) and len(element) > 0)
