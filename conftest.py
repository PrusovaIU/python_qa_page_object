from allure import attach, attachment_type
from contextlib import suppress
from datetime import datetime
from os import mkdir
from os.path import expanduser
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from sys import exc_info
from typing import Tuple
import logging
import pytest
import traceback


BROWSER = "--browser"
URL = "--url"
DRIVERS = "--drivers"
HEADLESS = "--headless"
ADMIN_NAME = "--user"
ADMIN_PASSWORD = "--password"


logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)s: %(name)-12s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger("DriverListener")


class DriverListener(AbstractEventListener):
    def before_click(self, element: WebElement, driver: WebDriver):
        logger.info(f"Element (Tag: {element.tag_name}) "
                    f"will be clicked on page {driver.current_url}")

    def on_exception(self, exception: Exception, driver: WebDriver):
        with suppress(FileExistsError):
            mkdir("logs")
        exception_info = exc_info()
        tb = str().join(traceback.format_tb(exception_info[2]))
        screenshot_url = f'logs/{type(exception).__name__}_{datetime.now()}.png'
        driver.save_screenshot(screenshot_url)
        logger.error(f"{tb}\tError: {type(exception).__name__}: {exception}")
        attach.file(
            source=screenshot_url,
            attachment_type=attachment_type.PNG
        )
        raise exception


def pytest_addoption(parser):
    parser.addoption(BROWSER, action="store", default="chrome")
    parser.addoption(URL, action="store", default="https://demo.opencart.com/")
    parser.addoption(DRIVERS, action="store", default=expanduser("~/Downloads/drivers"))
    parser.addoption(HEADLESS, action="store_true")
    parser.addoption(ADMIN_NAME, action="store", default="user")
    parser.addoption(ADMIN_PASSWORD, action="store", default="bitnami")


@pytest.fixture
def browser(request):
    browser = request.config.getoption(BROWSER)
    url = request.config.getoption(URL)
    drivers = request.config.getoption(DRIVERS)
    headless = request.config.getoption(HEADLESS)

    def add_options(options_type):
        options = options_type()
        options.headless = headless
        return options

    if browser == "chrome":
        chrome_options: webdriver.ChromeOptions = add_options(webdriver.ChromeOptions)
        chrome_options.add_experimental_option('w3c', False)
        caps = DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL', 'driver': 'ALL'}
        driver = webdriver.Chrome(executable_path=drivers + "/chromedriver",
                                  options=chrome_options, desired_capabilities=caps)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver",
                                   options=add_options(webdriver.FirefoxOptions))
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        raise Exception("Unknown browser")

    driver.maximize_window()
    driver = EventFiringWebDriver(driver, DriverListener())

    # def close_browser():
    #     if type(driver) is webdriver.Chrome:
    #         print(1)
    #     else:
    #         print(2)
    #     driver.close()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture
def admin(request) -> Tuple[str, str]:
    name = request.config.getoption(ADMIN_NAME)
    password = request.config.getoption(ADMIN_PASSWORD)
    return name, password
