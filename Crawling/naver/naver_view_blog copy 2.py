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
blog_dates = []

try:
    # 요소가 나타날 때까지 기다림
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.fds-inner-box.kV0SsxbyPm9jRwiQ8BLD a")
        )
    )

    # fds-inner-box 내의 a 태그 검색
    elements = driver.find_elements(By.CSS_SELECTOR, "div.fds-inner-box.kV0SsxbyPm9jRwiQ8BLD a")

    # 각 요소의 href 속성 수집
    for element in elements:
        blog_links.append(element.get_attribute("href"))

    # fds-inner-box 내의 날짜 정보 검색
    date_elements = driver.find_elements(
        By.CSS_SELECTOR, "div.fds-inner-box.kV0SsxbyPm9jRwiQ8BLD .fds-info-sub-inner-text"
    )

    # 각 요소의 텍스트 정보 수집
    for date_element in date_elements:
        blog_dates.append(date_element.text)

    # 수집된 블로그 링크와 날짜 정보 출력
    for link, date in zip(blog_links, blog_dates):
        print("Blog Link Found:", link, "Date:", date)

except TimeoutException:
    print("Timed out waiting for element to appear")

finally:
    driver.quit()
