from selenium.webdriver.common.by import By


class DashboardLocators:
    NAV_DASHBOARD = (By.XPATH, '//a[text()="My Dashboard"]')
    SEARCH = (By.ID, "search")
    LANGUAGE = (By.ID, "language")
    SORT = (By.ID, "sort")
    APPLY = (By.NAME, "commit")
