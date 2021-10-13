from selenium.webdriver.common.by import By
from typing import Tuple


LOCATOR_TYPE = Tuple[str, str]

IMG_LOCATOR = (By.TAG_NAME, "img")
INPUT_LOCATOR = (By.TAG_NAME, "input")
TD_LOCATOR = (By.TAG_NAME, "td")
