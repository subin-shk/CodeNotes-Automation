# fixture_lib/fixtures.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

# bring sensitive data like email and password from dotenv
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.nav_login_btn()
    login_page.enter_email(os.getenv("EMAIL"))
    login_page.enter_password(os.getenv("PASSWORD"))
    login_page.click_login_submit_button()
    return driver
