from webdriver_config import setup_chrome_driver

driver = setup_chrome_driver()

url = "https://www.naver.com"
driver.get(url)
