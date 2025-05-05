from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.dashboard_locators import DashboardLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def nav_to_dashboard(self):
        element = self.wait.until(
            EC.presence_of_element_located(DashboardLocators.NAV_DASHBOARD)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def search_codesnippet(self, term):
        element = self.wait.until(
            EC.presence_of_element_located(DashboardLocators.SEARCH)
        )
        self.driver.execute_script("arguments[0].value=arguments[1]", element, term)



    def apply(self):
        element = self.wait.until(
            EC.presence_of_element_located(DashboardLocators.APPLY)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def click_sort_dropdown(self, should_check=True):
        element = self.wait.until(
            EC.presence_of_element_located(DashboardLocators.SORT)
        )
        is_selected = self.driver.execute_script(
            "return arguments[0].checked;", element
        )
        if is_selected != should_check:
            self.driver.execute_script("arguments[0].click();", element)

    def select_a_z_sort(self, text):
        element = self.wait.until(
            EC.presence_of_element_located(DashboardLocators.A_Z_SORT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, text)

    def select_oldest_sort(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashboardLocators.OLDEST_SORT)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def search_result(self):
        result = self.wait.until(
            EC.presence_of_element_located(DashboardLocators.SEARCH_RESULT)
        )
        return self.driver.execute_script("return arguments[0].innerText;", result)
    def search_message(self):
        result = self.wait.until(
            EC.presence_of_element_located(DashboardLocators.SEARCH_MESSAGE)
        )
        return self.driver.execute_script("return arguments[0].innerText;", result)
