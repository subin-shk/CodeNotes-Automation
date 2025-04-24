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

    def select_language(self):
        try:
            # Wait for the dropdown to be clickable
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CodeSnippetsLocators.LANGUAGE_INPUT)
            )

            # Try using the Select method first
            select = Select(dropdown_element)
            select.select_by_visible_text("Kotlin")
        except Exception as e:
            print(f"[WARN] Standard select failed: {e}. Trying JS fallback...")

            # JavaScript fallback in case of Turbo or rendering issues
            try:
                self.driver.execute_script(
                    """
                    var select = document.getElementById('code_snippet_language');
                    var options = select.options;
                    for (var i = 0; i < options.length; i++) {
                        if (options[i].text === 'Kotlin') {
                            select.selectedIndex = i;
                            break;
                        }
                    }
                    select.dispatchEvent(new Event('change'));
                """
                )
            except JavascriptException as js_err:
                print(f"[ERROR] JavaScript execution failed: {js_err}")
                raise

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

    def view_card(self):
        view = self.driver.find_element(*CodeSnippetsLocators.VIEW)
        self.driver.execute_script("arguments[0].click();", view)
