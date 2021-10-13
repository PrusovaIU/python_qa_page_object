from page_objects.admin_pages.login_page import AdminLoginPage
from time import sleep


def test_add_new_good(browser, admin):
    AdminLoginPage(browser, f"{browser.current_url}/admin").login(admin[0], admin[1])


