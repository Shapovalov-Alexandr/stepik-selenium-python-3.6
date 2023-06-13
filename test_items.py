import time
import pytest
from selenium.webdriver.common.by import By


class TestCartButton:

    def test_presence_cart_button(self, browser):
        browser.implicitly_wait(6)
        browser.get(f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(11)

        # bool(...) возвращает True либо Fals
        assert bool(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")), "Add to cart button missing"
