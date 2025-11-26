"""
User registration tests.
Uses only fixtures to interact with elements.
"""

import pytest
from lesson_28.pages.login_page import LoginPageLocators
from lesson_28.pages.registration_page import RegistrationPageLocators
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
class TestRegistration:

    def test_registration_popup_opens(self, open_registration_popup):
        """Checking that the registration popup opened"""
        registration = open_registration_popup
        popup_title = registration.find_element(
            By.XPATH,
            "//h4[contains(@class, 'modal-title') and contains(text(), 'Registration')]"
        )
        assert popup_title.is_displayed()

    def test_registration_form_fields_exist(self, open_registration_popup):
        """Checking the presence of all fields in the registration form"""
        registration = open_registration_popup
        assert registration.find_element(*RegistrationPageLocators.NAME_INPUT).is_displayed()
        assert registration.find_element(*RegistrationPageLocators.LAST_NAME_INPUT).is_displayed()
        assert registration.find_element(*RegistrationPageLocators.EMAIL_INPUT).is_displayed()
        assert registration.find_element(*RegistrationPageLocators.PASSWORD_INPUT).is_displayed()
        assert registration.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).is_displayed()

    def test_successful_registration(self, fill_registration_form):
        """Verifying successful user registration"""
        page = fill_registration_form
        profile_header = page.find_element(
            *RegistrationPageLocators.PROFILE_HEADER
        )
        assert profile_header.is_displayed()

    def test_login_registered_user(self, open_login_popup):
        """
        Test login by user created in test:
            email: test.email5@example.com
            password: Password123!
        """
        page = open_login_popup

        page.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("test.email5@gmail.com")
        page.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("Password123!")
        page.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        logged_in = page.find_element(*RegistrationPageLocators.PROFILE_HEADER)
        assert logged_in.is_displayed()

if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])