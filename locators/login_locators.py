from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN = (By.XPATH, '//a[text()="Login"]')
    EMAIL_INPUT = (By.ID, "user_email")
    PASSWORD_INPUT = (By.ID, "user_password")
    LOGIN_SUBMIT = (By.NAME, "commit")
    LOGIN_ALERT = (By.XPATH, '//div[@role="alert"]')
    FORGOT_PASSWORD = (By.XPATH, "//div/a[text()='Forgot your password?']")
    # FORGOT_PASSWORD = (By.CSS_SELECTOR,'a[href="/users/password/new"')
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".mt-2.text-red-500.text-sm")
    
