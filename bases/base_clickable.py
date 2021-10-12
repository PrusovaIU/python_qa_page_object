from .base_element import BaseElement


class BaseClickable(BaseElement):
    def click(self) -> None:
        self._self.click()
