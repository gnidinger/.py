from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = setup_chrome_driver()

query = "마크 제이콥스 데이지"
url = "https://m.search.naver.com/search.naver?query="

driver.get(url + query)

blog_links = []

try:
    # 요소가 나타날 때까지 기다림
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".fds-thumb-simple-group .kV0SsxbyPm9jRwiQ8BLD a")
        )
    )

    # 요소 내의 모든 a 태그 검색
    elements = driver.find_elements(
        By.CSS_SELECTOR, ".fds-thumb-simple-group .kV0SsxbyPm9jRwiQ8BLD a"
    )

    # 각 요소의 href 속성 수집
    for element in elements:
        blog_links.append(element.get_attribute("href"))

    # 수집된 블로그 링크 출력
    for link in blog_links:
        print("Blog Link Found: ", link)

except TimeoutException:
    print("Timed out waiting for element to appear")

finally:
    driver.quit()
