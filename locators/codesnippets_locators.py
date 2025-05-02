from selenium.webdriver.common.by import By


class CodeSnippetsLocators:
    CODESNIPPETS = (By.XPATH, '//a[text()="Code Snippets"]')
    NEW_CODESNIPPETS = (By.XPATH, "//a[text()='New Code Snippet']")
    TITLE_INPUT = (By.ID, "code_snippet_title")
    LANGUAGE_INPUT = (By.ID, "code_snippet_language")
    DESCRIPTION_INPUT = (By.ID, "code_snippet_description")
    CODE_INPUT = (By.ID, "code_snippet_code")
    PRIVATE_CHECKBOX = (By.ID, "code_snippet_private")
    CREATE = (By.NAME, "commit")
    VIEW = (By.XPATH, "//div/a[text()='View']")
    TITLE_ERROR = (By.XPATH, "//input[@id='code_snippet_title']/following::p[1]")
    LANGUAGE_ERROR = (By.XPATH, "//select[@id='code_snippet_language']/following::p")
    CODE_ERROR = (By.XPATH, "//textarea[@id='code_snippet_code']/following::p")
    TAG_CHECKBOX_BY_LABEL = lambda label: (
        By.XPATH,
        f"//label[contains(normalize-space(), '{label}')]/preceding-sibling::input[@type='checkbox']",
    )

    @staticmethod
    def error_for_field(field_id):
        return (
            By.CSS_SELECTOR,
            f"#{field_id} ~ .error, #{field_id} ~ .text-red-500, #{field_id} ~ .field-error",
        )

    @staticmethod
    def VIEW_BUTTON_BY_TITLE(snippet_title):
        return (
            By.XPATH,
            f"//h5[contains(text(), '{snippet_title}')]/ancestor::div[contains(@class,'card')]//button[contains(text(),'View')]",
        )

    VIEW = (By.XPATH, "//div/a[text()='View']")
    EDIT = (By.XPATH, "//div/a[text()='Edit']")
