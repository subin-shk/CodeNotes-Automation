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

    # def select_language(self, language):
    #     select = Select(self.driver.find_element(By.XPATH, CodeSnippetsLocators.LANGUAGE_INPUT))
    #     select.select_by_value(language)
    # Locate the dropdown element
    # dropdown_element = self.wait.until(
    #     EC.presence_of_element_located(CodeSnippetsLocators.LANGUAGE_INPUT)
    # )

    # # Use JavaScript to select the value
    # self.driver.execute_script(
    #     "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
    #     dropdown_element,
    #     language,
    # )

    # def select_language(self, language):
    #     self.driver.execute_script(
    #         "arguments[0].click();",
    #         self.driver.find_element(*CodeSnippetsLocators.LANGUAGE_INPUT),
    #     )
    #     self.driver.find_element(By.XPATH, f"//*[text()='{language}']").click()

    # def languauge_select(self):
    #     element = self.driver.find_element(
    #         By.XPATH, CodeSnippetsLocators.LANGUAGE_INPUT
    #     )
    #     # element.click()
    #     element.send_keys("Kotlin")

    # def select_language(self):
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

    def alert(self):
        self.wait.until(EC.presence_of_element_located(LoginLocators.LOGIN_ALERT))

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*LoginLocators.LOGIN_ALERT),
        )
        return alert_text

    def view_card(self):
        view = self.driver.find_element(*CodeSnippetsLocators.VIEW)
        self.driver.execute_script("arguments[0].click();", view)
