from locators.kanji_locators import KanjiPageLocators


class KanjiPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_all_kanji(self):
        self.driver.find_element(*KanjiPageLocators.NAV_ALL_KANJI).click()

    def go_to_kanji_for_beginners(self):
        self.driver.find_element(*KanjiPageLocators.NAV_KANJI_FOR_BEGINNERS).click()

    def search_kanji(self, term):
        self.driver.find_element(*KanjiPageLocators.SEARCH_INPUT).send_keys(term)
        self.driver.find_element(*KanjiPageLocators.SEARCH_BUTTON).click()

    def get_kanji_cards(self):
        return self.driver.find_elements(*KanjiPageLocators.KANJI_CARDS)
