from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from locators.codesnippets_locators import CodeSnippetsLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CodeSnippetPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_snippet_btn(self):
        element = self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.CODESNIPPETS)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def click_new_snippet_btn(self):
        element = self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.NEW_CODESNIPPETS)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def enter_title(self, title):
        element = self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.TITLE_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, title)


    def select_language(self, language):
        # Locate the dropdown element
        dropdown_element = self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.LANGUAGE_INPUT)
        )

        # Use JavaScript to select the value
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
            dropdown_element,
            language,
        )

    def enter_description(self, description):
        element = self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.DESCRIPTION_INPUT)
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, description
        )

    def enter_code(self, code):
        element = self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.CODE_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, code)

    def submit_form(self):
        create_button = self.wait.until(
            EC.element_to_be_clickable(CodeSnippetsLocators.CREATE)
        )
        create_button.click()

    def get_success_message(self):
        try:
            # Adjust the selector for the success message based on your application
            success_message = self.wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "notice")
                )  # Modify this according to your app
            )
            return success_message.text
        except:
            return None
