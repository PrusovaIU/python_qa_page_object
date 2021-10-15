from page_objects.user_pages.bases.base_page_with_header import BasePageWithHeader
from page_objects.user_pages.elements.register_account_form import RegisterAccountForm


class AccountCabinetPage(BasePageWithHeader):
    @property
    def register_account_form(self) -> RegisterAccountForm:
        return RegisterAccountForm(self._browser)
