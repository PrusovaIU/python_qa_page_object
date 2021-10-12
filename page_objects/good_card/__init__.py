from bases.base_element import BaseElement
from bases.base_page import BasePage
from selenium.webdriver.common.by import By


class GoodCardPage(BasePage):
    BUTTON_CART_LOCATOR = (By.ID, "button-cart")

    @property
    def button_cart(self) -> BaseElement:
        return BaseElement(self._browser, self.BUTTON_CART_LOCATOR)
