from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.parse

driver = setup_chrome_driver()

query = "마크 제이콥스"
url = "https://search.shopping.naver.com/search/all?query="

driver.get(url + query)

decoded_values = []

try:
    # 일단 하나의 요소가 나타날 때까지 기다림
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-nclick]"))
    )

    # data-nclick 속성을 가진 모든 요소 검색
    elements = driver.find_elements(By.CSS_SELECTOR, "[data-nclick^='N=a:rel.keyword,i:']")

    # 각 요소를 출력
    for element in elements:
        nclick_value = element.get_attribute("data-nclick")
        # 'i:'와 ',' 사이의 값 추출
        encoded_str = nclick_value.split("i:")[1].split(",")[0]
        decoded_str = urllib.parse.unquote(encoded_str)
        decoded_values.append(decoded_str)

    for value in decoded_values:
        print("Decoded value: ", value)

except TimeoutException:
    print("Timed out waiting for element to appear")

finally:
    driver.quit()
