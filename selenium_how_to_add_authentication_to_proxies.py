from seleniumwire import webdriver
import time


# replace 'user:pass@ip:port' with your information
options = {
	'proxy': {
		'http': 'http://user:pass@ip:port',
		'https': 'https://user:pass@ip:port',
		'no_proxy': 'localhost,127.0.0.1'
	}
}

# replace 'your_absolute_path' with your chrome binary's aboslute path
driver = webdriver.Chrome('your_absolute_path', seleniumwire_options=options)

driver.get('http://whatismyipaddress.com')

time.sleep(8)

driver.quit()
