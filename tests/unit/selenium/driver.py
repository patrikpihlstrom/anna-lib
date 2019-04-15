import sys

from anna_lib.selenium.driver import create

desired_driver = 'chrome'
if len(sys.argv) > 1:
	desired_driver = sys.argv[1]

driver = create(driver=desired_driver, headless=True)
