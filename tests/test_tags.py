from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.login_page import LoginPage
from pages.tags_page import TagsPage
from locators.codesnippets_locators import CodeSnippetsLocators
from locators.kanji_locators import KanjiPageLocators
import time


class TestKanji:

    def test_nav_tag(self, driver):
        tags_page = TagsPage(driver)
        tags_page.click_tag_btn()
        time.sleep(3)
        expected = "Tags"
        actual = tags_page.tags_title()
        assert expected == actual, f"Failed: Expected {expected} but got {actual}"

    def test_new_tag(self, driver):
        tags_page = TagsPage(driver)
        tags_page.click_tag_btn()
        tags_page.click_new_tag()
        tags_page.send_name("New Tagg")
        tags_page.submit_name()
        expected = "Tag was successfully created."
        actual = tags_page.alert()
        assert expected == actual, f"Failed: Expected {expected} but got {actual}"
