from locators.kanji_locators import KanjiPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class KanjiPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def go_to_all_kanji(self):
        all_kanji = self.wait.until(
            EC.presence_of_element_located(KanjiPageLocators.NAV_ALL_KANJI)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", all_kanji)
        self.driver.execute_script("arguments[0].click();", all_kanji)

    def go_to_kanji_for_beginners(self):
        beginner_kanji = self.wait.until(
            EC.element_to_be_clickable(KanjiPageLocators.NAV_KANJI_FOR_BEGINNERS)
        )
        self.driver.execute_script("arguments[0].click();", beginner_kanji)

    def search_kanji(self, term):
        search_input = self.wait.until(
            EC.presence_of_element_located(KanjiPageLocators.SEARCH_INPUT)
        )
        search_button = self.wait.until(
            EC.presence_of_element_located(KanjiPageLocators.SEARCH_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_input)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", search_input, term
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
        self.driver.execute_script("arguments[0].click();", search_button)

    def get_kanji_cards(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(KanjiPageLocators.KANJI_CARDS)
        )

    def search_result(self):
        result_element = self.wait.until(
            EC.presence_of_element_located(KanjiPageLocators.SEARCH_RESULT)
        )
        return result_element.text.strip().lower()

    def click_kanji_card(self):
        cards = self.wait.until(
            EC.presence_of_all_elements_located(KanjiPageLocators.KANJI_CARDS)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cards[0])
        self.driver.execute_script("arguments[0].click();", cards[0])

    def video(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(KanjiPageLocators.ORDER_STROKE)
            )
            return True
        except TimeoutException:
            return False

    def mnemonics_presence(self):
        try:
            self.wait.until(EC.presence_of_element_located(KanjiPageLocators.MNEMONICS))
            return True
        except TimeoutException:
            return False
