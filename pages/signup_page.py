# from locators.signup_locators import SignupLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.signup_locators import SignupLocators


class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_signup_btn(self):
        element = self.wait.until(EC.presence_of_element_located(SignupLocators.SIGNUP))
        self.driver.execute_script("arguments[0].click();", element)

    def enter_email(self, email):
        element = self.wait.until(
            EC.presence_of_element_located(SignupLocators.EMAIL_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, email)

    def enter_password(self, password):
        element = self.wait.until(
            EC.presence_of_element_located(SignupLocators.PASSWORD_INPUT)
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, password
        )

    def enter_confirm_password(self, confirmpassword):
        element = self.wait.until(
            EC.presence_of_element_located(SignupLocators.CONFIRM_PASSWORD_INPUT)
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, confirmpassword
        )

    def click_signup_submit_button(self):
        button = self.wait.until(
            EC.presence_of_element_located(SignupLocators.SIGNUP_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", button)

    # Optional methods you can enable if needed
    # def is_logout_link_visible(self):
    #     element = self.wait.until(EC.presence_of_element_located(SignupLocators.LOGOUT_BUTTON))
    #     return element.text

    # def login_error_msg(self):
    #     return self.wait.until(EC.presence_of_element_located(SignupLocators.LOGIN_ERROR)).text
