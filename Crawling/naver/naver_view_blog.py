from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re

driver = setup_chrome_driver()

query = "마크 제이콥스 데이지 드림"
url = "https://m.search.naver.com/search.naver?query="

driver.get(url + query)

blog_info = []

try:
    # 블로그 주소와 작성 일자가 나타날 때까지 기다림
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='m.blog.naver.com']"))
    )

    # 블로그 주소에 해당하는 모든 요소 검색
    blog_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='m.blog.naver.com']")
    # 작성 일자에 해당하는 모든 요소 검색
    blog_dates = driver.find_elements(By.CSS_SELECTOR, "span[class='sub']")

    # 각 블로그 주소 및 작성 일자 정보 수집
    for i in range(len(blog_links)):
        blog_url = blog_links[i].get_attribute("href")
        # 블로그 주소에서 특정 부분 추출
        blogger_id = re.search(r"com/(\w+)", blog_url).group(1)
        blog_date = blog_dates[i].text

        blog_info.append((blogger_id, blog_date))

    for info in blog_info:
        print(f"Blogger ID: {info[0]}, Date: {info[1]}")

except TimeoutException:
    print("Timed out waiting for element to appear")

finally:
    driver.quit()
