import pytest
from selenium.common.exceptions import TimeoutException
from locators.signup_locators import SignupLocators


class TestSignup:
    def test_valid_signup(self, setup):
        driver, signup_page = setup

        signup_page.click_signup_btn()
        signup_page.enter_email("useradcdme@gmail.com")
        signup_page.enter_password("password123")
        signup_page.enter_confirm_password("password123")
        signup_page.click_signup_submit_button()

        expected = "Welcome! You have signed up successfully."
        actual = signup_page.signup_successful()
        assert actual == expected, "Failed: User was not able to sign up"
