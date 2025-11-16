import pytest
from homework_27 import TrackingNovaPoshtaPage

@pytest.mark.parametrize(
    "number, expected_status",
    [
        ("20400487562501", "Отримана")
    ]
)
def test_parcel_status(driver, number, expected_status):
    """
    Parametrized test that verifies the status returned from the tracking page.

    Steps:
    1. Open the tracking page.
    2. Enter the given parcel number.
    3. Click the search button.
    4. Validate that the displayed status matches the expected status.

    """
    page = TrackingNovaPoshtaPage(driver)
    page.open().enter_number(number).click_search()

    actual_status = page.get_status()

    assert actual_status == expected_status, \
        f"Expected '{expected_status}', but got '{actual_status}'"
