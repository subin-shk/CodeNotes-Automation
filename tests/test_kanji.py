import pytest
from pages.kanji_page import KanjiPage

def test_kanji_search_after_nav(driver):
    kanji_page = KanjiPage(driver)
    
    kanji_page.go_to_kanji_for_beginners()
    kanji_page.search_kanji("river")

    cards = kanji_page.get_kanji_cards()

    assert any("川" in card.text for card in cards), "Expected Kanji '川' not found in search results"
