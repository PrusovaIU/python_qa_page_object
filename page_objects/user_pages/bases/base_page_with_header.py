from page_objects.bases.base_page import BasePage
from page_objects.user_pages.elements.header import Header


class BasePageWithHeader(BasePage):
    @property
    def header(self):
        return Header(self._browser)
