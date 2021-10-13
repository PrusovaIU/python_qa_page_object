from page_objects.bases.base_element import BaseDefineElement
from page_objects.bases.CONSTS import LOCATOR_TYPE
from page_objects.bases.CONSTS import IMG_LOCATOR
from page_objects.bases.CONSTS import INPUT_LOCATOR
from page_objects.bases.CONSTS import TD_LOCATOR
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class Product:
    EDIT_BUTTON_LOCATOR = (By.CLASS_NAME, "btn-primary")

    def __init__(self, tr: WebElement):
        self._tr = tr
        items: List[WebElement] = self._tr.find_elements(*TD_LOCATOR)
        required_len = 8
        assert len(items) == required_len, f"Unknown format of tr. Expected {required_len} TD"
        self.__checkbox = self.__get_td_element(items[0], INPUT_LOCATOR)
        self.__image = self.__get_td_element(items[1], IMG_LOCATOR)
        self.__name = self.__get_td_text(items[2])
        self.__model = self.__get_td_text(items[3])
        self.__price = self.__get_td_text(items[4])
        self.__quantity = self.__get_td_text(items[5])
        self.__status = self.__get_td_text(items[6])
        self.__edit_button = self.__get_td_element(items[7], self.EDIT_BUTTON_LOCATOR)

    @staticmethod
    def __get_td_element(td: WebElement, locator: LOCATOR_TYPE):
        return td.find_element(*locator)

    @staticmethod
    def __get_td_text(td: WebElement):
        return td.text

    def select(self):
        self.__checkbox.click()


class ProductsTable(BaseDefineElement):
    ITEM_LOCATOR = (By.CSS_SELECTOR, "tbody > tr")

    @property
    def locator(self) -> LOCATOR_TYPE:
        return By.CSS_SELECTOR, "#form-product > table"

    def products(self):
        items: List[WebElement] = self._self.find_elements(*self.ITEM_LOCATOR)
        return [Product(item) for item in items]
