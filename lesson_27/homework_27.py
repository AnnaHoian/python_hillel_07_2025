from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrackingNovaPoshtaPage:
    """
    Page Object representing Nova Poshta tracking page.

    Provides methods to interact with the tracking UI elements:
        entering a parcel number,
        performing a search,
        retrieving the status.
    """

    INPUT_FIELD = (By.CSS_SELECTOR, ".track__form-group-input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".track__form-group-btn")
    STATUS_TEXT = (By.CSS_SELECTOR, ".header__status-text")

    def __init__(self, driver):
        """ Initializes the TrackingPage with a WebDriver instance."""

        self.driver = driver

    def open(self):
        """ Opens the tracking page."""

        self.driver.get("https://tracking.novaposhta.ua/#/uk")
        return self

    def enter_number(self, number):
        """ Enters the parcel number into the input field. """

        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_FIELD)
        )
        field.clear()
        field.send_keys(number)
        return self

    def click_search(self):
        """ Clicks the search button to submit the parcel tracking request. """
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()
        return self

    def get_status(self):
        """ Returns the status of the tracking page. """
        status = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.STATUS_TEXT)
        )
        return status.text
