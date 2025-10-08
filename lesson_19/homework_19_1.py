"""
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото, зробленi
ровером “Curiosity” на Марсi. Серед цих даних є посилання на фото, якi потрiбно розпарсити i потiм за допомогою
додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg, mars_photo2.jpg.
Завдання потрiбно зробити використовуючи модуль requests
"""

import requests
from requests.exceptions import HTTPError, RequestException

import logging

# basic configuration for logging
logging.basicConfig(
    filename="nasa_mars_photos_logger.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def download_mars_photos():
    """
    download_mars_photos function downloads Mars rover photos using NASA's open API.

    The function performs:
        - Sending an API request.
        - Validating the response status code.
        - Parsing JSON data to extract image URLs.
        - Downloading and saving each image locally as mars_photo1.jpg, mars_photo2.jpg.
        - Logging each step's result.

    Args:
        - Nasa API
        - Fixed parameters for the API request.
        - Nasa API test key

    Raises:
        - requests.exceptions.RequestException: If any network-related error occurs.
        - KeyError: If the JSON structure doesn't contain the expected fields.
    """

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

    try:
        # Send a request to the NASA API
        nasa_api_response = requests.get(url, params=params)
        nasa_api_response.raise_for_status()  # Raises an exception if the code is not 2xx

        # convert the response to JSON format
        data = nasa_api_response.json()
        logging.info(f"Data received: {data}")

        nasa_mars_photo_urls = []
        # iterate over all photos in the response and save them
        for photo_number, photo in enumerate(data['photos']):
            nasa_mars_photo_url = photo["img_src"]
            nasa_mars_photo_urls.append(nasa_mars_photo_url)

            # load and save locally each photo
            photo_response = requests.get(nasa_mars_photo_url)
            if photo_response.status_code == 200:
                # using wb (file opening mode for binary writing, without conversion to str)
                with open(f"mars_photo{photo_number + 1}.jpg", "wb") as file:
                    file.write(photo_response.content)
                    logging.info(f"Photo {photo_number + 1} saved successfully.")
            else:
                logging.error(f"Could not download photo {photo_number + 1}: status {photo_response.status_code}")

        # summary log
        logging.info(f"Total photos downloaded: {len(nasa_mars_photo_urls)}")

    except HTTPError as e:
        logging.error(f"HTTP error: {e}")

    except RequestException as e:
        logging.error(f"Network request error: {e}")

download_mars_photos()