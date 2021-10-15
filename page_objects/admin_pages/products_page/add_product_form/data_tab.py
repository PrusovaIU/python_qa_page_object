from .base_tab import BaseTab
from selenium.webdriver.common.by import By


class DataTab(BaseTab):
    MODEL_LOCATOR = (By.CSS_SELECTOR, "input#input-model")

    def fill(self, model: str):
        self._fill_input(self.MODEL_LOCATOR, model)
