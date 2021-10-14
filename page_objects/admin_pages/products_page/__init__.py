from .add_product_form import AddProductForm
from .filter import Filter
from .products_table import Product
from .products_table import ProductsTable
from ..bases.bases_admin_page import BaseAdminPage
from page_objects.bases.CONSTS import LOCATOR_TYPE
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List


class ProductsPage(BaseAdminPage):
    ADD_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".pull-right > a.btn-primary")
    DELETE_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".pull-right > button.btn.btn-danger")
    SAVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".pull-right > button.btn-primary")

    def add_product(self) -> AddProductForm:
        self.find_element(self.ADD_BUTTON_LOCATOR).click()
        return AddProductForm(self._browser, (By.TAG_NAME, "form"))

    def delete_product(self):
        self.find_element(self.DELETE_BUTTON_LOCATOR).click()

    def filter_products(self, product_name: str):
        Filter(self._browser).filter(product_name)

    def save(self):
        self.find_element(self.SAVE_BUTTON_LOCATOR).click()

    def get_products(self) -> List[Product]:
        return ProductsTable(self._browser).products()


def open_products_page(browser: WebDriver, admin_page: BaseAdminPage) -> ProductsPage:
    left_menu = admin_page.left_menu
    left_menu.catalog.click()
    new_url = left_menu.catalog.click_item(1)
    products_page = ProductsPage(browser, new_url, False)
    products_page.wait_browser_get_url(3)
    return products_page
