from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.switch_to import Alert


class BrowserAlert:
    def __init__(self, browser: WebDriver):
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        self._self: Alert = browser.switch_to.alert

    @property
    def text(self):
        return self._self.text

    def accept(self):
        self._self.accept()

    def dismiss(self):
        self._self.dismiss()
