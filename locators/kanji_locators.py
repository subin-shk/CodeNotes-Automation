from selenium.webdriver.common.by import By


class KanjiPageLocators:
    NAV_ALL_KANJI = (By.XPATH, '//a[text()="All Kanji"]')
    NAV_KANJI_FOR_BEGINNERS = (By.LINK_TEXT, "Kanji for Beginners")
    SEARCH_INPUT = (By.ID, "query")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Search']")
    KANJI_CARDS = (By.CLASS_NAME, "kanji-card")
    SEARCH_RESULT=(By.XPATH,"//p/span")
    ALERT = (By.XPATH, '//div[@role="alert"]')
    ORDER_STROKE=(By.TAG_NAME, 'video')
    MNEMONICS=(By.XPATH, "//h2[text()='Mnemonics']")
