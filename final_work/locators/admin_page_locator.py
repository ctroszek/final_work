from selenium.webdriver.common.by import By


class AdminPageLocator:
    LOCATOR_SHOULD_BE_ADMIN_PAGE = (
        By.XPATH, "//h1[contains(text(), 'Site administration')]"
    )
