from .base_page import BasePage
from abc import ABCMeta
from page_objects.elements.header import Header


class BasePageWithHeader(BasePage, metaclass=ABCMeta):
    @property
    def header(self):
        return Header(self._browser)
