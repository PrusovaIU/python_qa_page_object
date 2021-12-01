from logging import getLogger
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.switch_to import Alert


class BrowserAlert:
    def __init__(self, browser: WebDriver):
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        self._self: Alert = browser.switch_to.alert
        self._logger = getLogger(self.__class__.__name__)

    @property
    def text(self):
        return self._self.text

    def accept(self):
        self._self.accept()
        self._logger.info("Accept")

    def dismiss(self):
        self._self.dismiss()
        self._logger.info("Dismiss")
