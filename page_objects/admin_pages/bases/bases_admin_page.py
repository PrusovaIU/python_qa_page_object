from ..elements.left_menu import LeftMenu
from page_objects.bases.base_page import BasePage


class BaseAdminPage(BasePage):
    @property
    def left_menu(self) -> LeftMenu:
        return LeftMenu(self._browser)
