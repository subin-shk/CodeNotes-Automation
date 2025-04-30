from selenium.webdriver.common.by import By


class TagsLocators:
    NAV_TAGS = (By.XPATH, '//a[text()="Tags"]')
    TITLE = (By.XPATH, "//h1")
    NEW_TAG = (By.XPATH, '//a[text()="New Tag"]')
    NAME = (By.ID, "tag_name")
    SUBMIT = (By.NAME, "commit")
    ALERT = (By.XPATH, '//div[@role="alert"]')
