#!/usr/bin/python

import unittest
from tests.unit.selenium.driver import driver

loader = unittest.TestLoader()

suite = loader.discover('tests/unit/selenium')
print('found ' + str(suite.countTestCases()) + ' test cases')
unittest.TextTestRunner().run(suite)
driver.close()
driver.quit()
