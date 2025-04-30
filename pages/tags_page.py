from xml.dom.minidom import Element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.tags_locators import TagsLocators
from selenium.webdriver.common.by import By


class TagsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def click_tag_btn(self):
        element = self.wait.until(EC.presence_of_element_located(TagsLocators.NAV_TAGS))
        self.driver.execute_script("arguments[0].click();", element)

    def tags_title(self):
        element = self.wait.until(EC.presence_of_element_located(TagsLocators.TITLE))
        return self.driver.execute_script("return arguments[0].innerText;", element)

    def click_new_tag(self):
        element = self.wait.until(EC.presence_of_element_located(TagsLocators.NEW_TAG))
        self.driver.execute_script("arguments[0].click();", element)

    def send_name(self, name):
        element = self.wait.until(EC.presence_of_element_located(TagsLocators.NAME))
        self.driver.execute_script("arguments[0].value = arguments[1];", element, name)

    def submit_name(self):
        element = self.wait.until(EC.presence_of_element_located(TagsLocators.SUBMIT))
        self.driver.execute_script("arguments[0].click()", element)

    def alert(self):
        self.wait.until(EC.presence_of_element_located(TagsLocators.ALERT))

        # Use JavaScript Executor to retrieve the inner text of the element
        alert_text = self.driver.execute_script(
            "return arguments[0].innerText;",
            self.driver.find_element(*TagsLocators.ALERT),
        )
        return alert_text
