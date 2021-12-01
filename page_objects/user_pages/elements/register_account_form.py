from page_objects.bases.base_element import BaseDefineElement
from page_objects.bases.base_input import BaseInput
from page_objects.bases.CONSTS import LOCATOR_TYPE
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class RegisterAccountForm(BaseDefineElement):
    FIRSTNAME_INPUT_LOCATOR = (By.ID, "input-firstname")
    LASTNAME_INPUT_LOCATOR = (By.ID, "input-lastname")
    EMAIL_INPUT_LOCATOR = (By.ID, "input-email")
    TELEPHONE_INPUT_LOCATOR = (By.ID, "input-telephone")
    PASSWORD_INPUT_LOCATOR = (By.ID, "input-password")
    PASSWORD_CONFIRM_INPUT_LOCATOR = (By.ID, "input-confirm")
    SUBSCRIBE_LOCATOR = (By.CSS_SELECTOR, "input[type=radio]")
    PRIVACY_POLICY_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.btn.btn-primary[value='Continue']")

    @property
    def locator(self) -> LOCATOR_TYPE:
        return By.TAG_NAME, "#content > form"

    def __fill_input(self, locator: LOCATOR_TYPE, data: str):
        BaseInput(self._browser, locator, self._self).input(data)

    def fill(self, first_name: str, last_name: str, email: str,
             telephone: str, password: str, subscribe: bool):
        self.__fill_input(self.FIRSTNAME_INPUT_LOCATOR, first_name)
        self.__fill_input(self.LASTNAME_INPUT_LOCATOR, last_name)
        self.__fill_input(self.EMAIL_INPUT_LOCATOR, email)
        self.__fill_input(self.TELEPHONE_INPUT_LOCATOR, telephone)
        self.__fill_input(self.PASSWORD_INPUT_LOCATOR, password)
        self.__fill_input(self.PASSWORD_CONFIRM_INPUT_LOCATOR, password)
        subscribe_els: List[WebElement] = self._self.find_elements(*self.SUBSCRIBE_LOCATOR)
        radio = [el for el in subscribe_els if el.get_attribute("value") == str(int(subscribe))]
        radio[0].click()
        self.find_element(self.PRIVACY_POLICY_CHECKBOX_LOCATOR).click()
        self._logger.info(f"Fill data:"
                          f"\n\tFirst name: {first_name}"
                          f"\n\tLast name: {last_name}"
                          f"\n\tEmail: {email}"
                          f"\n\tTelephone: {telephone}"
                          f"\n\tPassword: {password}"
                          f"\n\tSubscribe: {subscribe}")
        return self

    def apply(self):
        self.find_element(self.CONTINUE_BUTTON_LOCATOR).click()
        self._logger.info("Button \"Continue\" has been clicked")
