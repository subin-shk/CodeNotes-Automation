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

    @pytest.mark.parametrize(
        "email, password, confirm_password, error_method, expected_error",
        [
            ("invalid-email", "password123", "password123", "get_email_error", "Email is invalid"),
            ("user@example.com", "password123", "password321", "get_password_mismatch_error", "Password confirmation doesn't match Password"),
            ("user@example.com", "123", "123", "get_password_length_error", "Password is too short (minimum is 6 characters)"),
        ],
    )
    def test_invalid_signup_cases(self, setup, email, password, confirm_password, error_method, expected_error):
        driver, signup_page = setup
        signup_page.click_signup_btn()
        signup_page.enter_email(email)
        signup_page.enter_password(password)
        signup_page.enter_confirm_password(confirm_password)
        signup_page.click_signup_submit_button()

        error_func = getattr(signup_page, error_method)
        actual_error = error_func()
        assert expected_error in actual_error, f"Failed: Expected '{expected_error}' but got '{actual_error}'"
