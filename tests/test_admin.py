from page_objects.admin_pages.bases.bases_admin_page import BaseAdminPage
from page_objects.admin_pages.products_page.add_product_form import AddProductForm
from page_objects.admin_pages.products_page.add_product_form.general_tab import GeneralTab
from page_objects.admin_pages.products_page.add_product_form.data_tab import DataTab
from page_objects.admin_pages.products_page.products_table import Product
from page_objects.admin_pages.login_page import AdminLoginPage
from page_objects.admin_pages.products_page import ProductsPage
from page_objects.admin_pages.products_page import open_products_page
from page_objects.elements.alert_success import AlertSuccess
from page_objects.elements.browser_alert import BrowserAlert
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List
from time import time as curtime


class NewProduct:
    def __init__(self, name: str, meta_tag_title: str, model: str):
        self.name = name
        self.meta_tag_title = meta_tag_title
        self.model = model


def add_new_good(current_browser: WebDriver, products_page: ProductsPage, new_product: NewProduct):
    new_product_form: AddProductForm = products_page.add_product()
    general_tab: GeneralTab = new_product_form.navtabs.general()
    general_tab.fill(new_product.name, new_product.meta_tag_title)
    data_tab: DataTab = new_product_form.navtabs.data()
    data_tab.fill(new_product.model)
    products_page.save()
    AlertSuccess(current_browser).close()


def delete_good(browser: WebDriver, products_page: ProductsPage, product: NewProduct):
    products_page.filter_products(product.name)
    products: List[Product] = products_page.get_products()
    products[0].select()
    products_page.delete_product()
    BrowserAlert(browser).accept()
    AlertSuccess(browser).close()


def test_add_delete_new_good(browser, admin):
    new_product = NewProduct(
        name=f"New_product_{curtime()}",
        meta_tag_title="New meta tag",
        model="New model"
    )
    AdminLoginPage(browser, f"{browser.current_url}/admin").login(admin[0], admin[1])
    products_page = open_products_page(
        browser,
        BaseAdminPage(browser, browser.current_url, False)
    )
    add_new_good(browser, products_page, new_product)
    delete_good(browser, products_page, new_product)
