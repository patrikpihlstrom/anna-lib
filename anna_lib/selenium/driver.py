from selenium import webdriver


def create(driver='firefox', headless=False, resolution=(1920, 1080)):
	"""
	Returns a webdriver based on the passed options
	"""
	if driver not in ('firefox', 'chrome'):
		raise TypeError

	if driver == 'chrome':
		options = webdriver.ChromeOptions()
	elif driver == 'firefox':
		options = webdriver.FirefoxOptions()

	options.headless = headless

	if driver == 'chrome':
		d = webdriver.Chrome(options=options, service_log_path='/dev/null')
	elif driver == 'firefox':
		d = webdriver.Firefox(options=options, service_log_path='/dev/null')

	if not (isinstance(resolution, (tuple, list)) and not (len(resolution) != 2) and not any(
			not isinstance(axis, int) for axis in resolution)):
		resolution = (1920, 1080)

	d.set_window_size(resolution[0], resolution[1])
	return d
