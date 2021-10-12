from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AlertSuccess:
    LOCATOR = (By.CSS_SELECTOR, ".alert-success")
    
    def __init__(self, browser: WebDriver):
        self.__browser: WebDriver = browser
        wait = WebDriverWait(browser, 2)
        wait.until(EC.visibility_of_element_located(self.LOCATOR))
        