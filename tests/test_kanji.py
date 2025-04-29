import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.login_page import LoginPage
from pages.kanji_page import KanjiPage
from locators.codesnippets_locators import CodeSnippetsLocators
from locators.login_locators import LoginLocators


class TestKanji:

    def test_search_kanji(self, driver):
        kanji_page = KanjiPage(driver)
        kanji_page.go_to_all_kanji()
        kanji_page.search_kanji("river")
        # expected = "river"
        # actual = kanji_page.search_result()
        # assert actual == expected, f"Failed: Expected '{expected}', but got '{actual}'"
