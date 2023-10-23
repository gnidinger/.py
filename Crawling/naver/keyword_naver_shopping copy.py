from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.parse
import time

driver = setup_chrome_driver()

query = "마크 제이콥스"
url = "https://shopping.naver.com/home"

driver.get(url)

decoded_values = []

try:
    # 일단 하나의 요소가 나타날 때까지 기다림
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#gnb-gnb > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div > input",
            )
        )
    )

    search_box = driver.find_element(
        By.CSS_SELECTOR,
        "#gnb-gnb > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div > input",
    )

    search_box.click()
    search_box.send_keys(query)
    time.sleep(1)
    search_box.send_keys(Keys.ARROW_DOWN * 2 + Keys.ENTER)

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
