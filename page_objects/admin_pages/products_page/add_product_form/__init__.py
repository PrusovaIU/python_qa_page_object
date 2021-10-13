from .data_tab import DataTab
from .general_tab import GeneralTab
from page_objects.bases.base_element import BaseElement
from selenium.webdriver.common.by import By


class NavTabs(BaseElement):
    def __enter(self, link_text: str):
        self.find_element((By.LINK_TEXT, link_text)).click()

    def general(self) -> GeneralTab:
        """Enter to general"""
        self.__enter("General")
        return GeneralTab(self._browser, (By.ID, "tab-general"))

    def data(self) -> DataTab:
        """Enter to data"""
        self.__enter("Data")
        return DataTab(self._browser, (By.ID, "tab-data"))


class AddProductForm(BaseElement):
    NAV_TABS_LOCATOR = (By.TAG_NAME, "ul")

    @property
    def navtabs(self) -> NavTabs:
        return NavTabs(self._browser, self.NAV_TABS_LOCATOR, self.web_element)
