from page_objects.bases.base_element import BaseElement
from page_objects.user_pages.bases.base_page_with_header import BasePageWithHeader
from selenium.webdriver.common.by import By


class GoodCardPage(BasePageWithHeader):
    BUTTON_CART_LOCATOR = (By.ID, "button-cart")

    @property
    def button_cart(self) -> BaseElement:
        return BaseElement(self._browser, self.BUTTON_CART_LOCATOR)
