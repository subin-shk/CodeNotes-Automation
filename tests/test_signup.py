import pytest
from selenium.common.exceptions import TimeoutException
from locators.signup_locators import SignupLocators
import uuid


class TestSignup:
    def test_valid_signup(self, setup):
        driver, signup_page = setup
        random_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
        signup_page.click_signup_btn()
        signup_page.enter_email(random_email)
        signup_page.enter_password("password123")
        signup_page.enter_confirm_password("password123")
        signup_page.click_signup_submit_button()

        expected = "Welcome! You have signed up successfully."
        actual = signup_page.signup_successful()
        assert actual == expected, "Failed: User was not able to sign up"
