from abc import ABCMeta, abstractmethod
from page_objects.bases.base_element import BaseElement
from page_objects.bases.CONSTS import LOCATOR_TYPE
from page_objects.bases.base_input import BaseInput
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Optional


class BaseTab(BaseElement, metaclass=ABCMeta):
    def __init__(self, browser: WebDriver, locator: LOCATOR_TYPE, parent: Optional[WebElement] = None):
        super(BaseTab, self).__init__(browser, locator, parent)
        self.wait_is_visible(3)

    def _fill_input(self, locator: LOCATOR_TYPE, data: str):
        BaseInput(self._browser, locator, self._self).input(data)

    @abstractmethod
    def fill(self, *args, **kwargs):
        pass
