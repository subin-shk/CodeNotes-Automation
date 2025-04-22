# from locators.signup_locators import SignupLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.signup_locators import SignupLocators
from selenium.webdriver.common.by import By

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

    def signup_successful(self):
        self.wait.until(
            EC.presence_of_element_located(SignupLocators.SIGNUP_SUCCESSFUL)
        )

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*SignupLocators.SIGNUP_SUCCESSFUL),
        )
        return alert_text

    def get_email_error(self):
        self.wait.until(EC.presence_of_element_located(SignupLocators.EMAIL_ERROR))

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*SignupLocators.EMAIL_ERROR),
        )

        return alert_text

    def get_password_mismatch_error(self):
        self.wait.until(
            EC.presence_of_element_located(SignupLocators.PASSWORD_MISMATCH_ERROR)
        )

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*SignupLocators.PASSWORD_MISMATCH_ERROR),
        )

        return alert_text

    def get_password_length_error(self):
        self.wait.until(
            EC.presence_of_element_located(SignupLocators.PASSWORD_SHORT_ERROR)
        )

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*SignupLocators.PASSWORD_SHORT_ERROR),
        )

        return alert_text
    
    # def get_all_errors(self):
    #     error_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'error') or contains(@class, 'text-red-500') or contains(text(), 'doesn't match')]")
    #     return [el.text.strip() for el in error_elements if el.is_displayed() and el.text.strip()]
