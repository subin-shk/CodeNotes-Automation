from selenium.webdriver.common.by import By


class DashboardLocators:
    NAV_DASHBOARD = (By.XPATH, '//a[text()="My Dashboard"]')
    SEARCH = (By.ID, "search")
    LANGUAGE = (By.ID, "language")
    SORT = (By.ID, "sort")
    APPLY = (By.NAME, "commit")
    OLDEST_SORT = (By.XPATH, '//option[@value="oldest"]')
    A_Z_SORT = (By.XPATH, '//option[@value="a-z"]')
