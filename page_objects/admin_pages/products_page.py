from .elements.add_product_form import AddProductForm
from .bases.bases_admin_page import BaseAdminPage
from selenium.webdriver.common.by import By


class ProductsPage(BaseAdminPage):
    ADD_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".pull-right > a.btn-primary")
    SAVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".pull-right > button.btn-primary")

    def add_product(self) -> AddProductForm:
        self.find_element(self.ADD_BUTTON_LOCATOR).click()
        return AddProductForm(self._browser, (By.TAG_NAME, "form"))
    
    def save(self):
        self.find_element(self.SAVE_BUTTON_LOCATOR).click()
