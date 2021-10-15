from .base_element import BaseElement


class BaseInput(BaseElement):
    def input(self, data: str):
        self._self.clear()
        self._self.send_keys(data)
