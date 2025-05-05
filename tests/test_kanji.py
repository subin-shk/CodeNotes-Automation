import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# from CodeNotes_Automation.pages import kanji_page
from pages.login_page import LoginPage
from pages.kanji_page import KanjiPage
from locators.codesnippets_locators import CodeSnippetsLocators
from locators.kanji_locators import KanjiPageLocators


class TestKanji:

    def test_search_kanji(self, driver):
        kanji_page = KanjiPage(driver)
        kanji_page.go_to_all_kanji()
        kanji_page.search_kanji("river")
        # expected = "river"
        # actual = kanji_page.search_result()
        # assert actual == expected, f"Failed: Expected '{expected}', but got '{actual}'"

    def test_search_empty(self, driver):
        kanji_page = KanjiPage(driver)
        kanji_page.go_to_all_kanji()

        kanji_page.search_kanji("")

        alert_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(KanjiPageLocators.ALERT)
        )

        actual = driver.execute_script(
            "return arguments[0].textContent;", alert_element
        ).strip()
        expected = f"Please enter a search term"

        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    def test_order_stroke(self, driver):
        kanji_page = KanjiPage(driver)
        kanji_page.go_to_all_kanji()
        kanji_page.click_kanji_card()
        assert kanji_page.video(), "Failed: Kanji detail do not have order stroke"
        
    def test_kanji_mneumonics(self, driver):
        kanji_page = KanjiPage(driver)
        kanji_page.go_to_all_kanji()
        kanji_page.click_kanji_card()
        assert kanji_page.mnemonics_presence(), "Failed: Kanji detail page do not have mneumonics"
        
        
