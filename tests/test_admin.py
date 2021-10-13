from page_objects.admin_pages.bases.bases_admin_page import BaseAdminPage
from page_objects.admin_pages.products_page.add_product_form import AddProductForm
from page_objects.admin_pages.products_page.add_product_form.general_tab import GeneralTab
from page_objects.admin_pages.products_page.add_product_form.data_tab import DataTab
from page_objects.admin_pages.login_page import AdminLoginPage
from page_objects.admin_pages.products_page import ProductsPage
from page_objects.admin_pages.products_page import open_products_page
from page_objects.elements.alert_success import AlertSuccess
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep, time as curtime


class Product:
    def __init__(self, name: str, meta_tag_title: str, model: str):
        self.name = name
        self.meta_tag_title = meta_tag_title
        self.model = model


def add_new_good(current_browser: WebDriver, products_page: ProductsPage, new_product: Product):
    new_product_form: AddProductForm = products_page.add_product()
    general_tab: GeneralTab = new_product_form.navtabs.general()
    general_tab.fill(new_product.name, new_product.meta_tag_title)
    data_tab: DataTab = new_product_form.navtabs.data()
    data_tab.fill(new_product.model)
    products_page.save()
    AlertSuccess(current_browser).close()


def test_add_delete_new_good(browser, admin):
    new_product = Product(
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
    sleep(2)



