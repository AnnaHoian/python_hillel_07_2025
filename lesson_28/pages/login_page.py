from selenium.webdriver.common.by import By

"""
Locators for the login page.
"""

class LoginPageLocators:
    EMAIL_INPUT = (By.ID, "signinEmail")
    PASSWORD_INPUT = (By.ID, "signinPassword")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-primary') and contains(text(), 'Login')]")

