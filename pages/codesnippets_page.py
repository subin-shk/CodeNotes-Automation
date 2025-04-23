from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from locators.codesnippets_locators import CodeSnippetsLocators
from selenium.webdriver.common.by import By


class CodeSnippetPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_new_snippet_btn(self):
        element = self.wait.until(EC.presence_of_element_located(CodeSnippetsLocators.NEW_CODESNIPPETS))
        self.driver.execute_script("arguments[0].click();", element)
