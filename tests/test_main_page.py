from page_objects.main_page import MainPage, MainPageElements
from time import sleep
from typing import Tuple
import pytest
from selenium.webdriver.common.by import By


def test_content(browser):
    sleep(1)
    MainPage(browser).find_element(MainPageElements.CONTENT)


@pytest.mark.parametrize("locator",
                         [
                             pytest.param(MainPageElements.SLIDESHOW, id="Test_slideshow"),
                             pytest.param(MainPageElements.ROW, id="Test_row"),
                             pytest.param(MainPageElements.CAROUSEL_SWIPER, id="Test_carousel")
                         ])
def test_find_elements(browser, locator: Tuple[str, str]):
    MainPage(browser).wait_visibility_of_element(locator, 3)


def test_button(browser):
    main_page = MainPage(browser)
    cart_button = main_page.header.cart_button
    cart_button.click()
    cart_ul = main_page.header.cart_ul
    cart_ul.wait_is_visible(3)
    required_text = "Your shopping cart is empty!"
    assert cart_ul.web_element.text == required_text, f"Unexpected text: {el.text}. \"{required_text}\" is expected"

