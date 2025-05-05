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
        language_element = self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.LANGUAGE_INPUT)
        )
        self.driver.execute_script(
            f"arguments[0].value = '{language}';", language_element
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

    def select_tag_by_label(self, label_text):
        locator = CodeSnippetsLocators.TAG_CHECKBOX_BY_LABEL(label_text)
        checkbox = self.wait.until(EC.presence_of_element_located(locator))
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def submit_form(self):
        try:
            create_button = self.wait.until(
                EC.element_to_be_clickable(CodeSnippetsLocators.CREATE)
            )
            create_button.click()
        except Exception as e:
            print(f"[WARN] Standard click failed: {e}. Trying JS fallback...")

            try:
                self.driver.execute_script(
                    """
                    const btn = document.querySelector("input[value='Create Snippet'], input[type='submit']");
                    if (btn) btn.click();
                """
                )
            except Exception as js_err:
                print(f"[ERROR] JS fallback failed: {js_err}")
                raise

    def view_card(self):
        view = self.driver.find_element(*CodeSnippetsLocators.VIEW)
        self.driver.execute_script("arguments[0].click();", view)

    def get_error_for_field(self, field_id):
        locator = CodeSnippetsLocators.error_for_field(field_id)
        return self.driver.find_element(*locator).text

    def get_title_error(self):
        self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.TITLE_ERROR)
        )

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*CodeSnippetsLocators.TITLE_ERROR),
        )

        return alert_text

    def get_language_error(self):
        self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.LANGUAGE_ERROR)
        )

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*CodeSnippetsLocators.LANGUAGE_ERROR),
        )

        return alert_text

    def get_code_error(self):
        self.wait.until(EC.presence_of_element_located(CodeSnippetsLocators.CODE_ERROR))

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*CodeSnippetsLocators.CODE_ERROR),
        )

        return alert_text

    def alert(self):
        self.wait.until(EC.presence_of_element_located(LoginLocators.LOGIN_ALERT))

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*LoginLocators.LOGIN_ALERT),
        )
        return alert_text

    # def click_view_by_title(self, snippet_title):
    #     view_button_locator = CodeSnippetsLocators.VIEW_BUTTON_BY_TITLE(snippet_title)
    #     view_button = self.wait.until(EC.element_to_be_clickable(view_button_locator))
    #     self.driver.execute_script("arguments[0].click();", view_button)

    def click_view(self):
        view_buttons = self.wait.until(
            EC.presence_of_all_elements_located(CodeSnippetsLocators.VIEW)
        )
        if view_buttons:
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", view_buttons[0]
            )
            self.driver.execute_script("arguments[0].click();", view_buttons[0])
        else:
            raise Exception("No view buttons found.")

    def click_edit(self):

        edit_button = self.wait.until(
            EC.presence_of_element_located(CodeSnippetsLocators.EDIT)
        )
        self.driver.execute_script("arguments[0].click();", edit_button)
        
