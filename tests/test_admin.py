from page_objects.admin_pages.bases.bases_admin_page import BaseAdminPage
from page_objects.admin_pages.elements.add_product_form import AddProductForm
from page_objects.admin_pages.elements.add_product_form.general_tab import GeneralTab
from page_objects.admin_pages.elements.add_product_form.data_tab import DataTab
from page_objects.admin_pages.login_page import AdminLoginPage
from page_objects.admin_pages.products_page import ProductsPage
from time import sleep


class Product:
    def __init__(self, name: str, meta_tag_title: str, model: str):
        self.name = name
        self.meta_tag_title = meta_tag_title
        self.model = model


def test_add_new_good(browser, admin):
    new_product = Product(
        name="New product",
        meta_tag_title="New meta tag",
        model="New model"
    )
    AdminLoginPage(browser, f"{browser.current_url}/admin").login(admin[0], admin[1])
    left_menu = BaseAdminPage(browser, browser.current_url, False).left_menu
    left_menu.catalog.click()
    new_url = left_menu.catalog.click_item(1)
    products_page = ProductsPage(browser, new_url, False)
    products_page.wait_browser_get_url(3)
    new_product_form: AddProductForm = products_page.add_product()
    general_tab: GeneralTab = new_product_form.navtabs.general()
    general_tab.fill(new_product.name, new_product.meta_tag_title)
    data_tab: DataTab = new_product_form.navtabs.data()
    data_tab.fill(new_product.model)
    sleep(2)



