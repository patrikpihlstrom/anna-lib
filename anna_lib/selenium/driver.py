from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def create(driver: str = 'firefox', headless: bool = True, resolution: tuple = (1920, 1080)) -> WebDriver:
	if driver not in ('firefox', 'chrome'):
		raise TypeError

	if driver == 'chrome':
		options = webdriver.ChromeOptions()
	elif driver == 'firefox':
		options = webdriver.FirefoxOptions()

	options.headless = headless

	if driver == 'chrome':
		d = webdriver.Chrome(options=options)
	elif driver == 'firefox':
		d = webdriver.Firefox(options=options)

	if not (isinstance(resolution, (tuple, list)) and not (len(resolution) != 2) and not any(
			not isinstance(axis, int) for axis in resolution)):
		resolution = (1920, 1080)

	d.set_window_size(resolution[0], resolution[1])
	return d
