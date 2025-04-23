import pytest
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.codesnippets_page import CodeSnippetPage

from locators.login_locators import LoginLocators


class TestNewSnippet:
    def test_new_snippet_without_login(self, driver):
        # driver, signup_page, login_page = setup
        code_page = CodeSnippetPage(driver)
        login_page = LoginPage(driver)
        code_page.click_new_snippet_btn()

        expected = "You need to sign in or sign up before continuing."
        actual = login_page.login_alert()
        assert (
            actual == expected
        ), "Failed: User was able to create new snippet without login"
