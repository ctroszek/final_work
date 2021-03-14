from pages.base_page import BasePage
from locators.admin_page_locator import AdminPageLocator


class AdminPage(BasePage):

    def should_be_admin_page(self):
        is_admin_page = self.find_element(
            AdminPageLocator.LOCATOR_SHOULD_BE_ADMIN_PAGE
        )
        assert is_admin_page.text == "Site administration"

