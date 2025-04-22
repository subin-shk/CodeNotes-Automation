from selenium.webdriver.common.by import By


class SignupLocators:
    SIGNUP = (By.XPATH, '//a[text()="Sign Up"]')
    EMAIL_INPUT = (By.ID, "user_email")
    PASSWORD_INPUT = (By.ID, "user_password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "user_password_confirmation")
    SIGNUP_BUTTON = (By.NAME, "commit")
    SIGNUP_SUCCESSFUL = (By.XPATH, '//div[@role="alert"]')
    EMAIL_ERROR = (By.XPATH, "//p[text()='Email is invalid']")
    PASSWORD_SHORT_ERROR = (
        By.XPATH,
        "//p[text()='Password is too short (minimum is 6 characters)']",
    )
    PASSWORD_MISMATCH_ERROR = (
        By.XPATH,
        '//p[text()="Password confirmation doesn\'t match Password"]',
    )
