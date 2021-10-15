from page_objects.bases.base_element import BaseElement
from page_objects.bases.CONSTS import LOCATOR_TYPE
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class MenuBlock(BaseElement):
    TITLE_LOCATOR = (By.TAG_NAME, 'a')
    LIST_LOCATOR = (By.TAG_NAME, 'ul')

    def __init__(self, browser: WebDriver, parent: WebElement, locator: LOCATOR_TYPE):
        super(MenuBlock, self).__init__(browser, locator, parent)
        self.__list = BaseElement(self._browser, self.LIST_LOCATOR, self._self)

    @property
    def title(self) -> BaseElement:
        return BaseElement(self._browser, self.TITLE_LOCATOR, self._self)

    @property
    def list(self) -> BaseElement:
        return self.__list

    def click_item(self, i: int) -> str:
        """
        Click to item of the menu
        :param i: item's position in menu
        :return: new url
        """
        items: List[WebElement] = self._self.find_elements_by_tag_name("li")
        required_item = items[i]
        a = required_item.find_element(By.TAG_NAME, 'a')
        new_url = a.get_attribute("href")
        required_item.click()
        return new_url


class LeftMenu(BaseElement):
    LOCATOR = (By.ID, "menu")
    CATALOG_LOCATOR = (By.ID, "menu-catalog")

    def __init__(self, browser: WebDriver):
        super(LeftMenu, self).__init__(browser, self.LOCATOR)

    def __get_menu_block(self, locator: LOCATOR_TYPE) -> MenuBlock:
        return MenuBlock(self._browser, self._self, locator)

    @property
    def catalog(self) -> MenuBlock:
        return self.__get_menu_block(self.CATALOG_LOCATOR)
