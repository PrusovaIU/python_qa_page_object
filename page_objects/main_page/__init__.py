from .featured_row import FeaturedRow
from bases.base_page_with_header import BasePageWithHeader
from selenium.webdriver.common.by import By


class MainPageElements:
    CONTENT = (By.ID, "content")
    SLIDESHOW = (By.ID, "slideshow0")
    ROW = (By.CLASS_NAME, "row")
    CAROUSEL_SWIPER = (By.ID, "carousel0")


class MainPage(BasePageWithHeader):
    @property
    def goods_row(self) -> FeaturedRow:
        return FeaturedRow(self._browser)
