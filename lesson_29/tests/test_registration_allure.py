"""
User registration tests with Allure reporting.
Tests include:
    - feature decorator
    - severity levels
    - step structure
"""

import pytest
import allure
from selenium.webdriver.common.by import By
from lesson_29.pages.login_page import LoginPageLocators
from lesson_29.pages.registration_page import RegistrationPageLocators


@allure.feature("User Registration and Login")
@pytest.mark.usefixtures("driver")
class TestRegistration:

    @allure.story("Open registration popup")
    @allure.title("Registration popup opens successfully")
    @allure.severity(allure.severity_level.NORMAL)
    def test_registration_popup_opens(self, open_registration_popup):
        """Check that the registration popup becomes visible."""
        with allure.step("Open registration popup"):
            registration = open_registration_popup

        with allure.step("Find popup title"):
            popup_title = registration.find_element(
                By.XPATH,
                "//h4[contains(@class, 'modal-title') and contains(text(), 'Registration')]"
            )

        with allure.step("Verify the popup is displayed"):
            assert popup_title.is_displayed()

    @allure.story("Check registration form elements")
    @allure.title("All required registration form fields are present")
    @allure.severity(allure.severity_level.MINOR)
    def test_registration_form_fields_exist(self, open_registration_popup):
        """Check that registration form fields exist and are visible."""
        registration = open_registration_popup

        with allure.step("Check NAME field exists"):
            assert registration.find_element(*RegistrationPageLocators.NAME_INPUT).is_displayed()

        with allure.step("Check LAST NAME field exists"):
            assert registration.find_element(*RegistrationPageLocators.LAST_NAME_INPUT).is_displayed()

        with allure.step("Check EMAIL field exists"):
            assert registration.find_element(*RegistrationPageLocators.EMAIL_INPUT).is_displayed()

        with allure.step("Check PASSWORD field exists"):
            assert registration.find_element(*RegistrationPageLocators.PASSWORD_INPUT).is_displayed()

        with allure.step("Check CONFIRM PASSWORD field exists"):
            assert registration.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).is_displayed()

    @allure.story("Successful user registration")
    @allure.title("User can successfully register with valid data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_registration(self, fill_registration_form):
        """Verify successful registration redirect to profile page."""
        with allure.step("Submit registration form"):
            page = fill_registration_form

        with allure.step("Verify profile header is displayed"):
            profile_header = page.find_element(*RegistrationPageLocators.PROFILE_HEADER)
            assert profile_header.is_displayed()

    @allure.story("Login as newly registered user")
    @allure.title("User can log in using previously registered credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_registered_user(self, open_login_popup):
        """
        Test login using a user created in registration test.
        Credentials:
            email: test.email9@gmail.com
            password: Password123!
        """
        page = open_login_popup

        with allure.step("Enter user email"):
            page.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("test.email9@gmail.com")

        with allure.step("Enter user password"):
            page.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("Password123!")

        with allure.step("Click Login button"):
            page.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        with allure.step("Verify that the user is logged in"):
            logged_in = page.find_element(*RegistrationPageLocators.PROFILE_HEADER)
            assert logged_in.is_displayed()


if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])
