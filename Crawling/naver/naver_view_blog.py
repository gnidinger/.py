from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = setup_chrome_driver()

query = "마크 제이콥스 데이지"
url = "https://m.search.naver.com/search.naver?query="

driver.get(url + query)

links = []

try:
    # today_hobby를 포함하는 링크 요소가 나타날 때까지 기다림
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='today_hobby']"))
    )

    # 모든 today_hobby를 포함하는 링크 요소 검색
    elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='today_hobby']")

    # 각 요소의 주소 수집
    for element in elements:
        links.append(element.get_attribute("href"))

    # 수집된 주소 출력
    for link in links:
        print("Link Found: ", link)

except TimeoutException:
    print("Timed out waiting for element to appear")

finally:
    driver.quit()
