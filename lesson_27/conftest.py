import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """
    Pytest fixture that initializes a Chrome WebDriver instance,
    provides it to the test, and ensures it closes after the test.

    """
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
