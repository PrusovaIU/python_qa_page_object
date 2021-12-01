from .CONSTS import LOCATOR_TYPE
from logging import getLogger
from os.path import normpath
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser: WebDriver, url: str, get: bool = True):
        self._logger = getLogger(self.__class__.__name__)
        self._url = url
        if get is True:
            browser.get(normpath(self._url))
        self._logger.info(f"Url: {browser.current_url}")
        self._browser = browser

    def find_element(self, locator: LOCATOR_TYPE) -> WebElement:
        """
        Find element on current page
        :param locator: (By, locators name)
        :return: found element or raise NoSuchElementException
        """
        return self._browser.find_element(*locator)

    def wait_browser_get_url(self, timeout: float):
        """
        Wait url is required url (self._url)
        :param timeout: timeout of waiting
        :return: None or raise TimeoutException
        """
        wait = WebDriverWait(self._browser, timeout)
        wait.until(EC.url_to_be(self._url))

    def wait_visibility_of_element(self, locator: LOCATOR_TYPE, timeout: float) -> None:
        """
        Wait the element is visible with timeout
        :param locator: (By, locators name)
        :param timeout: timeout of waiting
        :return: None or raise TimeoutException
        """
        wait = WebDriverWait(self._browser, timeout)
        wait.until(EC.visibility_of_element_located(locator))
