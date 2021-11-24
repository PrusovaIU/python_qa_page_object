from allure import step
from page_objects.elements.alert_success import AlertSuccess
from page_objects.user_pages.good_card import GoodCardPage
from page_objects.user_pages.main_page import MainPage
from selenium.webdriver.common.by import By


@step("Click on good")
def good_click(good) -> str:
    good_image = good.image
    good_url = good_image.find_element((By.TAG_NAME, 'a')).get_attribute("href")
    good_image.click()
    return good_url


def test_add_to_cart(browser):
    """Test add good to cart"""
    goods_row = MainPage(browser, browser.current_url).goods_row
    good = goods_row.goods[0]
    good_url = good_click(good)
    good_card_page = GoodCardPage(browser, good_url, False)
    good_card_page.wait_browser_get_url(3)
    good_card_page.button_cart.click()
    AlertSuccess(browser)
