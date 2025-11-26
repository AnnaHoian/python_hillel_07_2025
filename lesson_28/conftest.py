import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait

from lesson_28.pages.registration_page import RegistrationPageLocators

"""
Fixtures for testing user registration on the site.
Includes:
    driver: initializing the browser
    open_registration_popup: opening the registration form
    fill_registration_form: filling out the form and waiting for the profile
"""

@pytest.fixture
def driver():
    """Initializes Chrome browser and get the website"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()

@pytest.fixture
def open_login_popup(driver):
    """Opens the login form on the website"""
    wait = WebDriverWait(driver, 10)

    # Click "Sign In"
    sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.header_signin")))
    sign_in_button.click()

    # Wait for login pop up
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//h4[contains(@class, 'modal-title') and contains(text(), 'Log in')]")
    ))
    return driver

@pytest.fixture
def open_registration_popup(driver):
    """Opens the registration form on the website"""
    wait = WebDriverWait(driver, 10)

    # Click "Sign In"
    sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.header_signin")))
    sign_in_button.click()

    # Click "Registration"
    register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer .btn-link")))
    register_button.click()

    # Wait for registration pop up
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//h4[contains(@class, 'modal-title') and contains(text(), 'Registration')]")
    ))
    return driver

@pytest.fixture
def fill_registration_form(open_registration_popup):
    """Fills out the registration form and waits for successful registration"""
    registration = open_registration_popup
    wait = WebDriverWait(registration, 10)

    # Enter user data:

    registration.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Anna")
    registration.find_element(*RegistrationPageLocators.LAST_NAME_INPUT).send_keys("Sopilka")
    registration.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("test.email5@gmail.com")
    registration.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("Password123!")
    registration.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys("Password123!")

    # Click on "Register" button
    registration.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Wait for "My profile" page
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.PROFILE_HEADER))
    return registration

