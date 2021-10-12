from bases.base_element import BaseElement
from bases.CONSTS import LOCATOR_TYPE
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class ProductCard:
    IMAGE_LOCATOR = (By.CLASS_NAME, "image")
    CAPTION_LOCATOR = (By.CLASS_NAME, "caption")
    GROUP_BUTTON_LOCATOR = (By.CLASS_NAME, "button-group")

    def __init__(self, browser: WebDriver, product_div: WebElement):
        self.__browser: WebDriver = browser
        self.__div: WebElement = product_div

    def __get_element(self, locator: LOCATOR_TYPE) -> BaseElement:
        return BaseElement(self.__browser, locator, self.__div)

    @property
    def image(self) -> BaseElement:
        return self.__get_element(self.IMAGE_LOCATOR)

    @property
    def caption(self) -> BaseElement:
        return self.__get_element(self.CAPTION_LOCATOR)

    @property
    def group_button(self) -> BaseElement:
        return self.__get_element(self.GROUP_BUTTON_LOCATOR)


class FeaturedRow(BaseElement):
    def __init__(self, browser: WebDriver):
        super(FeaturedRow, self).__init__(browser, (By.CSS_SELECTOR, "#content > div.row"))
        goods_els: List[WebElement] = self.get_children()
        self.__goods = [ProductCard(browser, good) for good in goods_els]

    @property
    def goods(self) -> List[ProductCard]:
        return self.__goods
