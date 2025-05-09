from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def is_displayed(browser, locator):
    return WebDriverWait(browser, 15).until(
        ec.presence_of_element_located(
            (By.CSS_SELECTOR, locator)
        )
    )


def test_product_page_contains_add_to_cart_button(browser, page_url):
    browser.get(page_url)
    locator = '#add_to_basket_form > button[type="submit"]'

    assert is_displayed(browser, locator), \
        f'''Element not found with selector: {locator}'''


