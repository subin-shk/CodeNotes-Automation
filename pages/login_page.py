# from locators.signup_locators import SignupLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def nav_login_btn(self):
        element = self.wait.until(EC.presence_of_element_located(LoginLocators.LOGIN))
        self.driver.execute_script("arguments[0].click();", element)

    def enter_email(self, email):
        element = self.wait.until(
            EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, email)

    def enter_password(self, password):
        element = self.wait.until(
            EC.presence_of_element_located(LoginLocators.PASSWORD_INPUT)
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, password
        )

    def click_login_submit_button(self):
        button = self.wait.until(
            EC.presence_of_element_located(LoginLocators.LOGIN_SUBMIT)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def login_alert(self):
        self.wait.until(EC.presence_of_element_located(LoginLocators.LOGIN_ALERT))

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*LoginLocators.LOGIN_ALERT),
        )
        return alert_text

    def click_forgot_password(self):
        forgot_password = self.wait.until(
            EC.presence_of_element_located(LoginLocators.FORGOT_PASSWORD)
        )
        self.driver.execute_script("arguments[0].click()", forgot_password)


    def enter_email_in_forgot_password_field(self, email):
        send_email = self.wait.until(
            EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", send_email, email
        )

    def error_message(self):
        return self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*LoginLocators.ERROR_MESSAGE),
        )
