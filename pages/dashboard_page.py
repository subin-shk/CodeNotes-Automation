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
            EC.presence_of_all_elements_located(DashboardLocators.SEARCH)
        )
        self.driver.execute_script("arguments[0].value=arguments[1]", element, term)
        
    def apply(self):
        element = self.wait.until(
            EC.presence_of_element_located(DashboardLocators.APPLY)
        )
        self.driver.execute_script("arguments[0].click();", element)      

    