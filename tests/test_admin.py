from page_objects.admin_pages.bases.bases_admin_page import BaseAdminPage
from page_objects.admin_pages.login_page import AdminLoginPage
from time import sleep


def test_add_new_good(browser, admin):
    AdminLoginPage(browser, f"{browser.current_url}/admin").login(admin[0], admin[1])
    left_menu = BaseAdminPage(browser, browser.current_url, False).left_menu
    left_menu.catalog.click()
    left_menu.catalog.click_item(1)
    sleep(1)



