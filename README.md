## anna-lib

The purpose of this package is to simplify the use of selenium.

### requirements
[selenium](https://pypi.org/project/selenium/),
[anna-common](https://pypi.org/project/anna-common/),
[anna-unittasks](https://pypi.org/project/anna-unittasks/)

### installation
```bash
$ pip install anna-lib
```

### usage
```python
from anna_lib.selenium import driver, events, assertions


result = []
firefox = driver.create({'driver': 'firefox', 'headless': True})

firefox.get('http://example.com/')
events.click(firefox, 'a[href="http://www.iana.org/domains/example"')

result.append(assertions.current_url_is(firefox, 'http://www.iana.org/domains/example'))
```

### driver

### events

### assertions
