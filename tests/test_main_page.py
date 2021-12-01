from .attach_sreenshot import attach_screenshot
from page_objects.user_pages.main_page import MainPage, MainPageElements
from page_objects.user_pages.elements.header.top_panel import CURRENCY
from typing import Tuple
import allure
import pytest


def test_content(browser):
    MainPage(browser, browser.current_url).find_element(MainPageElements.CONTENT)


@pytest.mark.parametrize("locator",
                         [
                             pytest.param(MainPageElements.SLIDESHOW, id="Test_slideshow"),
                             pytest.param(MainPageElements.ROW, id="Test_row"),
                             pytest.param(MainPageElements.CAROUSEL_SWIPER, id="Test_carousel")
                         ])
def test_find_elements(browser, locator: Tuple[str, str]):
    """
    Test find element
    """
    try:
        allure.dynamic.title(f"Test find element: {locator}")
        MainPage(browser, browser.current_url).wait_visibility_of_element(locator, 3)
    except Exception as err:
        attach_screenshot(browser, err)
        raise err


@allure.title("Test click on button")
def test_button(browser):
    """
    Test click on cart button of empty cart
    """
    try:
        main_page = MainPage(browser, browser.current_url)
        with allure.step("Click on cart button"):
            cart_button = main_page.header.cart_button
            cart_button.click()
        cart_ul = main_page.header.cart_ul
        cart_ul.wait_is_visible(3)
        required_text = "Your shopping cart is empty!"
        assert cart_ul.web_element.text == required_text, f"Unexpected text: {cart_ul.web_element.text}. " \
                                                          f"\"{required_text}\" is expected"
    except Exception as err:
        attach_screenshot(browser, err)
        raise err


@allure.title("Test change currency")
def test_change_currency(browser):
    """Test change currency on top panel"""
    try:
        main_page = MainPage(browser, browser.current_url)
        main_page.top_panel.change_currency(CURRENCY.GBP)
    except Exception as err:
        attach_screenshot(browser, err)
        raise err
