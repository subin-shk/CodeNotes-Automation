import pytest
from selenium import webdriver
from pages.signup_page import SignupPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(
        "https://ns-code-snippet-9eae23357ebe.herokuapp.com/"
    )  
    signup_page = SignupPage(driver)
    yield driver, signup_page
    driver.quit()
