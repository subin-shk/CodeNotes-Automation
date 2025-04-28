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
        snippet_page.select_tag_by_label("hello world")
        snippet_page.select_tag_by_label("1")
        snippet_page.select_tag_by_label("खुला स्रोत")
        snippet_page.submit_form()

        expected = "Code snippet was successfully created."
        actual = login_page.login_alert()
        assert actual == expected, "Failed: User was not able to create new snippet"
        
        # @pytest.mark.parametrize(
    #     "title, language, code, expected_field",
    #     [
    #         ("", "Python", "print('Hello')", "code_snippet_title"),  # Missing title
    #         (
    #             "Valid Title",
    #             "",
    #             "print('Hello')",
    #             "code_snippet_language",
    #         ),  # Missing language
    #         ("Valid Title", "Python", "", "code_snippet_code"),  # Missing code
    #         (
    #             "",
    #             "",
    #             "",
    #             "code_snippet_title",
    #         ),  # All missing, check first error (title)
    #     ],
    # )
    # def test_snippet_required_fields(
    #     self, driver, title, language, code, expected_field
    # ):
    #     login_page = LoginPage(driver)
    #     snippet_page = CodeSnippetPage(driver)

    #     # Login
    #     login_page.click_login_btn()
    #     login_page.enter_email("test@example.com")
    #     login_page.enter_password("test123")
    #     login_page.click_login_submit_button()

    #     # Navigate
    #     snippet_page.click_snippet_btn()
    #     snippet_page.click_new_snippet_btn()

    #     # Fill form
    #     if title:
    #         snippet_page.enter_title(title)
    #     if language:
    #         snippet_page.select_language(language)
    #     if code:
    #         snippet_page.enter_code(code)

    #     snippet_page.submit_form()

    #     # Wait for error to show up for the expected field
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located(
    #             CodeSnippetsLocators.error_for_field(expected_field)
    #         )
    #     )

    #     error_text = snippet_page.get_error_for_field(expected_field)
    #     assert (
    #         "can't be blank" in error_text.lower()
    #     ), f"Expected 'can't be blank' for {expected_field}, but got: {error_text}"

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