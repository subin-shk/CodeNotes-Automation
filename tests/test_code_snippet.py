import pytest
from selenium.common.exceptions import TimeoutException

from pages.login_page import LoginPage
from pages.codesnippets_page import CodeSnippetPage

from locators.login_locators import LoginLocators


class TestNewSnippet:
    def test_new_snippet_without_login(self, driver):
        # driver, signup_page, login_page = setup
        snippet_page = CodeSnippetPage(driver)
        login_page = LoginPage(driver)
        snippet_page.click_new_snippet_btn()

        expected = "You need to sign in or sign up before continuing."
        actual = login_page.login_alert()
        assert (
            actual == expected
        ), "Failed: User was able to create new snippet without login"

    # def test_new_snippet(self, driver):
    #     snippet_page = CodeSnippetPage(driver)
    #     login_page = LoginPage(driver)
    #     login_page.click_login_btn()
    #     login_page.enter_email("test@example.com")
    #     login_page.enter_password("test123")
    #     login_page.click_login_submit_button()

    #     import time

    #     time.sleep(5)
    #     snippet_page.click_snippet_btn()

    #     snippet_page.click_new_snippet_btn()
    #     snippet_page.enter_title("Example Snippet Title")
    #     snippet_page.select_language("Kotlin")
    #     snippet_page.enter_description(
    #         "This is a sample description for a code snippet."
    #     )
    #     snippet_page.enter_code("print('Hello, world!')")

    #     # Submit the form
    #     snippet_page.submit_form()
