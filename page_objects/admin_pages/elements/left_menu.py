from page_objects.bases.base_element import BaseElement
from page_objects.bases.CONSTS import LOCATOR_TYPE
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class MenuBlock:
    TITLE_LOCATOR = (By.TAG_NAME, 'a')
    LIST_LOCATOR = (By.TAG_NAME, 'ul')

    def __init__(self, browser: WebDriver, menu_block: WebElement):
        self.__browser = browser
        self.__menu_block = menu_block

    @property
    def title(self) -> BaseElement:
        return BaseElement(self.__browser, self.TITLE_LOCATOR, self.__menu_block)

    def list(self) -> BaseElement:
        return BaseElement(self.__browser, self.LIST_LOCATOR, self.__menu_block)


class LeftMenu(BaseElement):
    LOCATOR = (By.ID, "menu")
    CATALOG_LOCATOR = (By.ID, "menu-catalog")

    def __init__(self, browser: WebDriver):
        super(LeftMenu, self).__init__(browser, self.LOCATOR)

    def __get_menu_block(self, locator: LOCATOR_TYPE) -> MenuBlock:
        menu_block = self.find_element(locator)
        return MenuBlock(self._browser, menu_block)

    @property
    def catalog(self) -> MenuBlock:
        return self.__get_menu_block(self.CATALOG_LOCATOR)
