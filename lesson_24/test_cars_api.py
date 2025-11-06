import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

"""
Pytest API testing for Cars Flask application.
    - Uses pytest fixture for authenticated session reuse
    - Parameterized tests with multiple sorting/limit combinations
    - Logging of requests, responses, and validation results
    - Validation of:
        * Status codes (200, 400)
        * Data structure (list of dicts)
        * Record limits
        * Presence of required fields
        * Correct sorting where applicable
"""

# --------------------------
# Logger Settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('cars_search_logs.log')
console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# --------------------------
# Authentication fixture

@pytest.fixture(scope="class")
def auth_session():
    """Fixture to authenticate user and provide a session with JWT token."""
    session = requests.Session()
    url = "http://127.0.0.1:8080/auth"
    response = session.post(
        url,
        auth = HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200, "Authentication failed"
    access_token = response.json().get('access_token')
    session.headers.update({'Authorization': 'Bearer ' + access_token})

    logger.info("Authentication successful")
    return session

# --------------------------
# Parametrized test

@pytest.mark.parametrize("sort_by, limit",
                         [
                             ("price", 3),
                             ("year", 5),
                             ("brand", 2),
                             ("engine_volume", 4),
                             ("price", 1),
                             ("price", 0), # edge case
                             ("invalid_field", 3), # invalid field
                         ],
                         ids=[
                             "price_3", "year_5", "brand_2", "engine_4",
                             "price_1", "limit_0", "invalid_sort"
                         ]
)

class TestCarsAPI:
    """Class for checking car search with parameters"""
    def test_car_search(self, auth_session, sort_by, limit):
        """Tests car search API endpoint with sorting and limit parameters."""
        params = {"sort_by": sort_by, "limit": limit}
        url = "http://127.0.0.1:8080/cars"

        logger.info(f"Start test: sort_by={sort_by}, limit={limit}")

        resp = auth_session.get(url, params=params)
        logger.info(f"-Request URL: {resp.request.url}")
        logger.info(f"-Request status: {resp.status_code}")

        # Status check
        assert resp.status_code in (200, 400)

        if resp.status_code == 400:
            logger.warning(f"Bad request for sort_by={sort_by}, limit={limit}")
            return

        data = resp.json()
        logger.info(f"Returned {len(data)} records")

        # Type check
        assert isinstance(data, list), f"Response must be a list"

        # Limit check
        if limit > 0:
            assert len(data) <= limit, f"Returned more than {limit} records"

        # Structure check
        if data:
            sample = data[0]
            for key in ("brand", "year", "engine_volume", "price"):
                assert key in sample, f"Missing key: {key}"
            logger.info(f"Returned {len(sample)} records")

        # Sorting check
        if data and sort_by in data[0]:
            values = [item [sort_by] for item in data]
            try:
                sorted_values = sorted(values)
                assert values == sorted_values, f"Data not sorted by {sort_by}"
                logger.info(f"Sorting by {sort_by} succeeded")
            except TypeError:
                logger.warning(f"Cannot sort by {sort_by}")

        logger.info(f"End test: sort_by={sort_by}, limit={limit}")



