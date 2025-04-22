import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.signup_page import SignupPage


@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument("--window-size=1920,1080")  # Optional, but useful
    options.add_argument("--no-sandbox")  # Good for CI environments
    options.add_argument("--disable-dev-shm-usage")  # Prevent resource issues

    driver = webdriver.Chrome(options=options)
    driver.get("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    signup_page = SignupPage(driver)

    yield driver, signup_page
    driver.quit()
