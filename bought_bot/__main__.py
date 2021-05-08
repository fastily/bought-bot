

from time import sleep

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with Chrome() as driver:
    #your code inside this indent
    driver.get("https://www.bestbuy.com/site/apple-airtag/6461348.p?skuId=6461348")
    # e = driver.find_element_by_css_selector("button[data-sku-id='6461348']")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-sku-id='6461348']"))
    )

    sleep(3)
    print(element.text)
    print(element.tag_name)
    print(element.parent)
    print(element.location)
    print(element.size)
    # sleep(10)

