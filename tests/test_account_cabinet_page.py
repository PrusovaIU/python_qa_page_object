from .attach_sreenshot import attach_screenshot
from allure import title
from page_objects.user_pages.account_cabinet_page import AccountCabinetPage
from page_objects.user_pages.bases.base_page_with_header import BasePageWithHeader
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import time as curtime


@title("Test adding new user")
def test_add_new_user(browser):
    """
    Test adding new user
    """
    try:
        BasePageWithHeader(browser, browser.current_url, False).top_panel.register_new_user()
        account_cabinet_page = AccountCabinetPage(browser, browser.current_url, False)
        user_id = curtime()
        account_cabinet_page.register_account_form.fill(
            first_name=f"User name {user_id}",
            last_name=f"User lastname {user_id}",
            email=f"email{user_id}@mail.com",
            telephone="+79990009900",
            password="111111",
            subscribe=False
        ).apply()
        WebDriverWait(browser, 3).until(EC.url_contains("account/success"))
    except Exception as err:
        attach_screenshot(browser, err)
        raise err
