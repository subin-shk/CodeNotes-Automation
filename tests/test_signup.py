import pytest
from selenium.common.exceptions import TimeoutException


class TestSignup:
    def test_valid_signup(self, setup):
        driver, signup_page = setup

        signup_page.click_signup_btn()
        signup_page.enter_email("username@gmail.com")
        signup_page.enter_password("password123")
        signup_page.enter_confirm_password("password123")
        signup_page.click_signup_submit_button()

        # Optional: Assert URL change or success message
        # expected_url = "https://quotes.toscrape.com/login"
        # actual_url = driver.current_url
        # assert actual_url != expected_url, "Failed: User was not able to sign up"
