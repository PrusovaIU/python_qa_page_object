from page_objects.bases.base_element import BaseElement
from page_objects.bases.base_input import BaseInput
from page_objects.bases.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AdminLoginPage(BasePage):
    USERNAME_INPUT_LOCATOR = (By.ID, "input-username")
    PASSWORD_INPUT_LOCATOR = (By.ID, "input-password")
    BUTTON_LOCATOR = (By.CLASS_NAME, "btn-primary")

    def login(self, user_name: str, password: str):
        BaseInput(self._browser, self.USERNAME_INPUT_LOCATOR).input(user_name)
        BaseInput(self._browser, self.PASSWORD_INPUT_LOCATOR).input(password)
        BaseElement(self._browser, self.BUTTON_LOCATOR).click()
        WebDriverWait(self._browser, 3).until(EC.url_changes(self._url))
