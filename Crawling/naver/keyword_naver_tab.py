from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = setup_chrome_driver()

query = "마크 제이콥스 데이지"

url = "https://m.search.naver.com/search.naver?query="

driver.get(url + query)

try:
    # 일단 하나의 요소가 나타날 때까지 기다림
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a._slog_visible"))
    )

    # 가장 처음 요소 하나만 검색
    element = driver.find_element(By.CSS_SELECTOR, "a._slog_visible")

    print("Element: ", element.text)

    # 모든 요소 검색
    elements = driver.find_elements(By.CSS_SELECTOR, "a._slog_visible")

    # 각 요소를 출력
    for element in elements:
        print("Element Found: ", element.text)

except TimeoutException:
    print("Timed out waiting for element to appear")

finally:
    driver.quit()
