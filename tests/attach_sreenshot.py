from allure import attach, attachment_type
from contextlib import suppress
from datetime import datetime
from os import mkdir
from selenium.webdriver.remote.webdriver import WebDriver


def attach_screenshot(driver: WebDriver, exception: Exception):
    with suppress(FileExistsError):
        mkdir("logs")
    screenshot_url = f'logs/{type(exception).__name__}_{datetime.now()}.png'
    driver.save_screenshot(screenshot_url)
    attach.file(
        source=screenshot_url,
        attachment_type=attachment_type.PNG
    )
