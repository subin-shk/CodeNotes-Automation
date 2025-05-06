import pytest
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage

from locators.login_locators import LoginLocators
import time


class TestLogin:
    def test_valid_login(self, logged_in_driver):
        login_page = LoginPage(logged_in_driver)

        expected = "Signed in successfully."
        actual = login_page.login_alert()
        assert actual == expected, "Failed: User was not able to login"

    @pytest.mark.parametrize(
        "email, password, expected_error",
        [
            (
                "invalid@gmail.com",
                "password123",
                "Invalid Email or password.",
            ),
            (
                "",
                "",
                "Invalid Email or password.",
            ),
        ],
    )
    def test_invalid_login(self, driver, email, password, expected_error):
        login_page = LoginPage(driver)
        login_page.nav_login_btn()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_submit_button()

        expected = expected_error
        actual = login_page.login_alert()
        assert actual == expected, "Failed: User was not able to login"

    def test_invalid_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.nav_login_btn()
        time.sleep(1)
        login_page.click_forgot_password()
        time.sleep(3)
        login_page.enter_email_in_forgot_password_field("testcom")
        login_page.click_login_submit_button()
        time.sleep(3)
        assert (
            "Email not found" in login_page.error_message()
        ), "Failed: User was able to submit invalid email"
    def test_empty_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.nav_login_btn()
        time.sleep(1)
        login_page.click_forgot_password()
        time.sleep(3)
        login_page.enter_email_in_forgot_password_field("")
        login_page.click_login_submit_button()
        time.sleep(3)
        assert (
            "Email can't be blank" in login_page.error_message()
        ), "Failed: User was able to submit empty email"
