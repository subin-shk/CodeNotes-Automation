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

    def test_invalid_email(self, setup):
        driver, signup_page = setup
        signup_page.click_signup_btn()
        signup_page.enter_email("invalid-email")
        signup_page.enter_password("password123")
        signup_page.enter_confirm_password("password123")
        signup_page.click_signup_submit_button()

        error = signup_page.get_email_error()
        assert "Email is invalid" in error, "Failed: Invalid email was accepted"

    def test_password_mismatch(self, setup):
        driver, signup_page = setup
        random_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
        signup_page.click_signup_btn()
        signup_page.enter_email(random_email)
        signup_page.enter_password("password123")
        signup_page.enter_confirm_password("password321")
        signup_page.click_signup_submit_button()

        error = signup_page.get_password_mismatch_error()
        assert (
            "Password confirmation doesn't match Password" in error
        ), "Failed: Mismatched passwords accepted"

    def test_password_too_short(self, setup):
        driver, signup_page = setup
        random_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
        signup_page.click_signup_btn()
        signup_page.enter_email(random_email)
        signup_page.enter_password("123")
        signup_page.enter_confirm_password("123")
        signup_page.click_signup_submit_button()

        error = signup_page.get_password_length_error()
        assert (
            "Password is too short (minimum is 6 characters)" in error
        ), "Failed: Short password accepted"
