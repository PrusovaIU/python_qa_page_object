from bases.base_clickable import BaseClickable
from bases.base_element import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Header(BaseElement):
    def __init__(self, browser: WebDriver):
        super(Header, self).__init__(browser, (By.TAG_NAME, "header"))

    @property
    def cart_button(self):
        return BaseClickable(self._browser, (By.CSS_SELECTOR, "#cart > button"), self._self)

    @property
    def cart_ul(self):
        return BaseElement(self._browser, (By.CSS_SELECTOR, "#cart > ul"), self._self)
