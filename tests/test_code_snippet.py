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

    def test_new_snippet(self, driver):
        snippet_page = CodeSnippetPage(driver)
        login_page = LoginPage(driver)
        login_page.click_login_btn()
        login_page.enter_email("test@example.com")
        login_page.enter_password("test123")
        login_page.click_login_submit_button()

        import time

        time.sleep(5)
        snippet_page.click_snippet_btn()

        snippet_page.click_new_snippet_btn()
        snippet_page.enter_title("Example Snippet Title")

        snippet_page.select_language("Kotlin")
        snippet_page.enter_description(
            "This is a sample description for a code snippet."
        )
        snippet_page.enter_code("print('Hello, world!')")
        snippet_page.select_tag_by_label("new")
        snippet_page.select_tag_by_label("1")
        # snippet_page.select_tag_by_label("खुला स्रोत")
        snippet_page.submit_form()

        expected = "Code snippet was successfully created."
        actual = login_page.login_alert()
        assert actual == expected, "Failed: User was not able to create new snippet"

    @pytest.mark.parametrize(
        "title, language, description, code,error_method, expected_error",
        [
            (
                "",
                "Kotlin",
                "hello word",
                "print('Hello, world!')",
                "get_title_error",
                "Title can't be blank",
            ),
            (
                "Hello World",
                "",
                "hello word",
                "print('Hello, world!')",
                "get_language_error",
                "Language can't be blank",
            ),
            (
                "Hello World",
                "Kotlin",
                "hello word",
                "",
                "get_code_error",
                "Code can't be blank",
            ),
        ],
    )
    def test_empty_required_fields(
        self, driver, title, language, description, code, error_method, expected_error
    ):
        snippet_page = CodeSnippetPage(driver)
        login_page = LoginPage(driver)
        login_page.click_login_btn()
        login_page.enter_email("test@example.com")
        login_page.enter_password("test123")
        login_page.click_login_submit_button()

        import time

        time.sleep(5)
        snippet_page.click_snippet_btn()

        snippet_page.click_new_snippet_btn()
        snippet_page.enter_title(title)

        snippet_page.select_language(language)
        snippet_page.enter_description(description)
        snippet_page.enter_code(code)
        snippet_page.submit_form()

        error_func = getattr(snippet_page, error_method)
        actual_error = error_func()
        assert (
            expected_error in actual_error
        ), f"Failed: Expected '{expected_error}' but got '{actual_error}'"

    def test_view_card(self, driver):
        snippet_page = CodeSnippetPage(driver)
        login_page = LoginPage(driver)
        login_page.click_login_btn()
        login_page.enter_email("test@example.com")
        login_page.enter_password("test123")
        login_page.click_login_submit_button()

        import time

        time.sleep(5)
        snippet_page.click_snippet_btn()
        time.sleep(5)
        snippet_page.view_card()
