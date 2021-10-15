from .base_tab import BaseTab
from selenium.webdriver.common.by import By


class GeneralTab(BaseTab):
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, "input#input-name1")
    DESCRIPTION_LOCATOR = (By.CLASS_NAME, "note-editable")
    META_TAG_TITLE_LOCATOR = (By.CSS_SELECTOR, "input#input-meta-title1")
    META_TAG_DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, "textarea#input-meta-description1")
    META_TAG_KEYWORDS_LOCATOR = (By.CSS_SELECTOR, "textarea#input-meta-keyword1")
    PRODUCT_TAGS_LOCATOR = (By.CSS_SELECTOR, "input#input-tag1")

    def fill(self, product_name: str, meta_tag_title: str, description: str = '',
             meta_tag_description: str = '', meta_tag_key_words: str = '', product_tags: str = ''):
        self._fill_input(self.PRODUCT_NAME_LOCATOR, product_name)
        self._fill_input(self.DESCRIPTION_LOCATOR, description)
        self._fill_input(self.META_TAG_TITLE_LOCATOR, meta_tag_title)
        self._fill_input(self.META_TAG_DESCRIPTION_LOCATOR, meta_tag_description)
        self._fill_input(self.META_TAG_KEYWORDS_LOCATOR, meta_tag_key_words)
        self._fill_input(self.PRODUCT_TAGS_LOCATOR, product_tags)
