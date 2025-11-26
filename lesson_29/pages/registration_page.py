from selenium.webdriver.common.by import By

"""
Locators for the registration page.
"""

class RegistrationPageLocators:
    NAME_INPUT = (By.ID, "signupName")
    LAST_NAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    CONFIRM_PASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-primary') and contains(text(), 'Register')]")

    PROFILE_HEADER = (By.CSS_SELECTOR, ".user-nav.dropdown")