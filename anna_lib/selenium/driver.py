from selenium import webdriver


def create(options):
	"""
	Returns a webdriver based on the passed options
	"""
	if 'driver' not in options:
		raise KeyError
	if options['driver'] not in ('firefox', 'chrome'):
		raise TypeError

	if options['driver'] == 'chrome':
		o = webdriver.ChromeOptions()
	elif options['driver'] == 'firefox':
		o = webdriver.FirefoxOptions()

	o.headless = options['headless']

	if options['driver'] == 'chrome':
		driver = webdriver.Chrome(options=o, service_log_path='/dev/null')
	elif options['driver'] == 'firefox':
		driver = webdriver.Firefox(options=o, service_log_path='/dev/null')

	resolution = tuple(str(options['resolution']).split('x')) if 'resolution' in options and options[
		'resolution'] is not None else (1920, 1080)
	driver.set_window_size(resolution[0], resolution[1])

	return driver
