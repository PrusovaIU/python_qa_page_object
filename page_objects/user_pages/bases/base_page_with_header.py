from page_objects.bases.base_page import BasePage
from page_objects.user_pages.elements.header import Header
from page_objects.user_pages.elements.header.top_panel import TopPanel


class BasePageWithHeader(BasePage):
    @property
    def header(self):
        return Header(self._browser)

    @property
    def top_panel(self) -> TopPanel:
        return TopPanel(self._browser)
