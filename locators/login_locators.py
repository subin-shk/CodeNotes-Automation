from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN = (By.XPATH, '//a[text()="Login"]')
    EMAIL_INPUT = (By.ID, "user_email")
    PASSWORD_INPUT = (By.ID, "user_password")
    LOGIN_SUBMIT = (By.NAME, "commit")
    LOGIN_SUCCESSFUL = (By.XPATH, '//div[@role="alert"]')
