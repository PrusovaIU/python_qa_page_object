from .add_product_form import AddProductForm
from .filter import Filter
from ..bases.bases_admin_page import BaseAdminPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsPage(BaseAdminPage):
    ADD_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".pull-right > a.btn-primary")
    SAVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".pull-right > button.btn-primary")

    def add_product(self) -> AddProductForm:
        self.find_element(self.ADD_BUTTON_LOCATOR).click()
        return AddProductForm(self._browser, (By.TAG_NAME, "form"))

    def filter_products(self, product_name: str):
        Filter(self._browser).filter(product_name)

    def save(self):
        self.find_element(self.SAVE_BUTTON_LOCATOR).click()


def open_products_page(browser: WebDriver, admin_page: BaseAdminPage) -> ProductsPage:
    left_menu = admin_page.left_menu
    left_menu.catalog.click()
    new_url = left_menu.catalog.click_item(1)
    products_page = ProductsPage(browser, new_url, False)
    products_page.wait_browser_get_url(3)
    return products_page
