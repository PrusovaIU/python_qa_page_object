from .CONSTS import LOCATOR_TYPE
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from typing import Optional


class _ElementHasLocator:
    def __init__(self, element: WebElement, locator: LOCATOR_TYPE):
        self.__element: WebElement = element
        self.__locator: LOCATOR_TYPE = locator

    def __call__(self, driver: WebDriver):
        try:
            return self.__element.find_element(*self.__locator)
        except NoSuchElementException:
            return False


class BaseElement:
    def __init__(self, browser: WebDriver, locator: LOCATOR_TYPE, parent: Optional[WebElement] = None):
        self._browser: WebDriver = browser
        self._parent: Optional[WebElement] = parent
        if parent is None:
            self._parent = self._browser.find_element_by_tag_name("body")
        self._self: WebElement = self._parent.find_element(*locator)

    @property
    def web_element(self) -> WebElement:
        return self._self

    def find_element(self, locator: LOCATOR_TYPE) -> WebElement:
        """
        Find element in this element
        :param locator: (By, locators name)
        :return: found element or raise NoSuchElementException
        """
        return self._self.find_element(*locator)

    def wait_is_visible(self, timeout: float):
        """
        Wait the self is visible
        :return: None or raise TimeoutException
        """
        wait = WebDriverWait(self._browser, timeout)
        wait.until(EC.visibility_of(self._self))

    def wait_visibility_of_element(self, locator: LOCATOR_TYPE, timeout: float) -> None:
        """
        Wait the element in self is visible with timeout
        :param locator: (By, locators name)
        :param timeout:
        :return: None or raise TimeoutException
        """
        wait = WebDriverWait(self._browser, timeout)
        wait.until(_ElementHasLocator(self._self, locator))
