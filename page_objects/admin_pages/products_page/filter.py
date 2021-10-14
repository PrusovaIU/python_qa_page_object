from page_objects.bases.base_element import BaseDefineElement
from page_objects.bases.base_input import BaseInput
from page_objects.bases.CONSTS import LOCATOR_TYPE
from selenium.webdriver.common.by import By


class Filter(BaseDefineElement):
    PRODUCT_NAME_INPUT_LOCATOR = (By.ID, "input-name")
    FIND_BUTTON_LOCATOR = (By.ID, "button-filter")

    @property
    def locator(self) -> LOCATOR_TYPE:
        return By.ID, "filter-product"

    def filter(self, product_name: str):
        product_name_input = BaseInput(self._browser, self.PRODUCT_NAME_INPUT_LOCATOR, self._self)
        product_name_input.input(product_name)
        self.find_element(self.FIND_BUTTON_LOCATOR).click()
