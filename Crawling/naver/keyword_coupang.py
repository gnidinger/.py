from webdriver_config import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = setup_chrome_driver()

query = "마크 제이콥스 향수"
url = "https://www.coupang.com/np/search?component=&q="

driver.get(url + query)

product_texts = []
price_texts = []

try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.name")))

    # 모든 요소 검색
    elements = driver.find_elements(By.CSS_SELECTOR, "div.name")

    # 각 요소의 텍스트 수집
    for element in elements:
        product_texts.append(element.text)

    prive_elements = driver.find_elements(By.CSS_SELECTOR, "div.price > em > strong")

    for price_element in prive_elements:
        price_texts.append(price_element.text)

    # 수집된 텍스트 출력
    for product, price in zip(product_texts, price_texts):
        print("Product: ", product, "Price: ", price + "원")

except TimeoutException:
    print("Timed out waiting for element to appear")

finally:
    driver.quit()
