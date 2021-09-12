from configparser import ConfigParser
from time import sleep
from contextlib import suppress

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_element(driver: WebDriver, selector: str, strategy: str = By.CSS_SELECTOR, timeout: int = 10) -> WebElement:
    with suppress(Exception):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((strategy, selector)))


def _main() -> None:
    """main driver, to be run when this script is invoked directly"""

    (config := ConfigParser()).read("config.ini")
    config = config["Best Buy"]

    with Chrome() as driver:
        driver.get(config["url"])

        while not (add_to_cart := fetch_element(driver, "button.c-button-primary.add-to-cart-button")):  # "button.btn-primary[data-sku-id='6410839']"
            sleep(5)
            driver.refresh()

        # add item to cart and start checkout
        add_to_cart.click()
        driver.get("https://www.bestbuy.com/cart")
        sleep(10)
        fetch_element(driver, "div.checkout-buttons__checkout > button").click()

        # apparently it's easier to just login
        fetch_element(driver, "#fld-e").send_keys(config["username"])
        fetch_element(driver, "#fld-p1").send_keys(config["password"])
        fetch_element(driver, "button[data-track='Sign In']").click()
        sleep(10)

        # navigate to checkout page
        # driver.get("https://www.bestbuy.com/checkout/r/payment")
        fetch_element(driver, "#cvv").send_keys(config["cvv"])

        # sometimes billing address fields appear
        if fn := fetch_element(driver, "payment.billingAddress.firstName", By.ID):
            fn.send_keys(config["first_name"])
            fetch_element(driver, "payment.billingAddress.lastName", By.ID).send_keys(config["last_name"])
            fetch_element(driver, "payment.billingAddress.street", By.ID).send_keys(config["street"])
            fetch_element(driver, "payment.billingAddress.city", By.ID).send_keys(config["city"])

            Select(fetch_element(driver, "payment.billingAddress.state", By.ID)).select_by_visible_text(config["state"])
            fetch_element(driver, "payment.billingAddress.zipcode", By.ID).send_keys(config["zip"])

        # order
        if (element := fetch_element(driver, "button.btn-primary[data-track='Place your Order - Contact Card'")) and config.get("live"):
            element.click()
        else:
            print(element.text)
            print(element.tag_name)
            print(element.parent)
            print(element.location)

        print("reached the end, did we get it?")
        sleep(20)


if __name__ == "__main__":
    _main()
