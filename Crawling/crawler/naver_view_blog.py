from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = setup_chrome_driver()

query = "마크 제이콥스 데이지 드림"
url = "https://m.search.naver.com/search.naver?query="

driver.get(url + query)

blog_links = []
blog_dates = []

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.fds-article-box-header a"))
    )

    elements = driver.find_elements(By.CSS_SELECTOR, "div.fds-article-box-header a")
    for element in elements:
        blog_links.append(element.get_attribute("href"))

    date_elements = driver.find_elements(By.CSS_SELECTOR, "span.fds-info-sub-inner-text")
    for date_element in date_elements:
        # 가져온 텍스트에서 '·' 문자를 기준으로 나눈 후 두 번째 부분을 선택하여 앞뒤 공백을 제거
        blog_dates.append(date_element.text.split("·")[1].strip())

    for link, date in zip(blog_links, blog_dates):
        print("Blog Link Found:", link, "Date:", date)

except TimeoutException:
    print("Timed out waiting for element to appear")

finally:
    driver.quit()
