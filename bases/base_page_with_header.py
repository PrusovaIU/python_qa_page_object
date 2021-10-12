from .base_page import BasePage
from page_objects.elements.header import Header


class BasePageWithHeader(BasePage):
    @property
    def header(self):
        return Header(self._browser)
