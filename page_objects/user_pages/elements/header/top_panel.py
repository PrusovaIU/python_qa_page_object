from page_objects.bases.base_element import BaseDefineElement
from page_objects.bases.CONSTS import LOCATOR_TYPE
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TopPanel(BaseDefineElement):
    ACCOUNT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown > a")
    ACCOUNT_MENU_LOCATOR = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown > ul")

    @property
    def locator(self) -> LOCATOR_TYPE:
        return By.ID, "top"

    def _click_account_menu(self, link_text: str):
        current_url = self._browser.current_url
        self.find_element(self.ACCOUNT_BUTTON_LOCATOR).click()
        self.wait_visibility_of_element(self.ACCOUNT_MENU_LOCATOR, 3)
        menu: WebElement = self.find_element(self.ACCOUNT_MENU_LOCATOR)
        menu.find_element(By.LINK_TEXT, link_text).click()
        WebDriverWait(self._browser, 3).until(EC.url_changes(current_url))

    def register_new_user(self):
        self._click_account_menu("Register")
