import pytest
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage

from locators.login_locators import LoginLocators


class TestLogin:
    def test_valid_login(self, driver):
        # driver, signup_page, login_page = setup
        login_page=LoginPage(driver)
        login_page.click_login_btn()
        login_page.enter_email("test@example.com")
        login_page.enter_password("test123")

        login_page.click_login_submit_button()

        expected = "Signed in successfully."
        actual = login_page.login_successful()
        assert actual == expected, "Failed: User was not able to login"
