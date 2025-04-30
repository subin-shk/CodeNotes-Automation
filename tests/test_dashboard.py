import pytest
from selenium.common.exceptions import TimeoutException

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from locators.login_locators import LoginLocators
import time


class TestDashboard:
    def test_search(self, logged_in_driver):
        dashboard_page = DashboardPage(logged_in_driver)
        dashboard_page.nav_to_dashboard()
        time.sleep(3)
        dashboard_page.search_codesnippet("test")
        dashboard_page.apply()
