from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.parse

driver = setup_chrome_driver()

query = "마크 제이콥스"

url = "http://suggestqueries.google.com/complete/search?output=toolbar&q="

driver.get(url + query)

suggested_keywords = []

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "suggestion"))
    )

    elements = driver.find_elements(By.CSS_SELECTOR, "suggestion")

    for element in elements:
        suggested_data = element.get_attribute("data")
        suggested_keywords.append(suggested_data)

    for keyword in suggested_keywords:
        print("Suggested keyword: ", keyword)

except TimeoutException:
    print("Timed out waiting for element to appear")
finally:
    driver.quit()
