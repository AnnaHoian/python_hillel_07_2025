"""
У venv Python встановiть Flask за допомогою команди pip install flask +

Створiть у окремiй директорiї файл app.py та скопiюйте у нього код файлу app.py
який приведено нижче в початкових даних. +

Запустiть http сервер за допомогою команди python app.py +
Сервер стартує за базовою адресою http://127.0.0.1:8080

Враховуючи документацiю яку наведено нижче вам потрiбно написати код який використовуючи модуль request
зробить через POST upload якогось зображення на сервер, за допомогою GET отримає посилання на цей файл
і потiм за допомогою DELETE зробить видалення файлу з сервера
"""

import requests
from urllib.parse import quote # for encoding filename in URL
import logging

# basic configuration for logging
logging.basicConfig(
    filename="remote_server_photos_logger.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ImageUploadingToServer:
    def __init__(self, base_url: str):
        """
        Args:
            base_url (str): base server URL
        """
        self._base_url = base_url
        self._uploaded_filename = None

    def upload_image(self, image_path: str):
        """
        Uploads an image to the server (POST /upload)

        Args:
            image_path (str): image file path
        """
        try:
            with open(image_path, 'rb') as image:
                files = {"image": image}
                response = requests.post(f"{self._base_url}/upload", files=files)
                response.raise_for_status()

                if response.status_code == 201:
                    data = response.json()
                    image_url= data.get("image_url")
                    logging.info(f"Image is downloaded successfully! URL: {image_url}")
                    self._uploaded_filename = image_url
                    return image_url
                else:
                    logging.error(f"Received unexpected status: {response.status_code}")
                    return None

        except requests.exceptions.RequestException as e:
            logging.error(f"POST request failed: {e}")
            return None
        except FileNotFoundError:
            logging.error(f"File {image_path} is not found")
            return None


    def get_image(self, filename: str):
        """
        Gets an image or its URL.
        Args:
            - filename: the name of the file on the server
        Returns:
            - str: Image URL if Content-Type is text
            - None: if the image itself is returned
        """

        try:
            # encode filename for URL
            encoded_filename = quote(filename, safe="")
            url = f"{self._base_url}/image/{encoded_filename}"

            response = requests.get(url)
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            logging.info(f"Content-Type: {content_type}")

            if "json" in content_type or content_type.startswith("text"):
                data = response.json()
                image_url = data.get("image_url")
                logging.info(f"Received Image URL: {image_url}")
                return image_url

            elif content_type.startswith("image"):
                local_filename = "downloaded_" + filename
                with open(local_filename, "wb") as local_file:
                    local_file.write(response.content)
                logging.info(f"Image saved locally as {local_filename}")
                return local_filename

            else:
                logging.error(f"Unsupported content type: {content_type}")
                return None

        except requests.exceptions.RequestException as e:
            logging.error(f"GET request failed: {e}")
            return None

    def delete_image(self, filename: str):
        """

        Deletes an image from the server.

        Args:
            - filename (str): the name of the file to be deleted

        Returns:
            - JSON with a message on success or None on error

        """

        try:
            encoded_filename = quote(filename, safe="")
            url = f"{self._base_url}/delete/{encoded_filename}"

            response = requests.delete(url)
            response.raise_for_status()

            if response.status_code == 200:
                data = response.json()
                logging.info(f"Image deleted successfully! Response: {data}")
                return data

            else:
                logging.error(f"Received unexpected delete status: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            logging.error(f"DELETE request failed: {e}")
            return None



server = ImageUploadingToServer('http://127.0.0.1:8080')

# download the image to server
upload_image = server.upload_image(r"C:\Users\Public\Pictures\file_example_JPG.jpg")

# get downloaded image URL
get_image_URL= server.get_image("file_example_JPG.jpg")

# delete the image from the server
delete_image = server.delete_image("file_example_JPG.jpg")


