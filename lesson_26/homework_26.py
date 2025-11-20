from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import logging

# log file configurations
logging.basicConfig(
    filename="dz_frames.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Secret text each frame

SECRET_TEXT1 = "Frame1_Secret"
SECRET_TEXT2 = "Frame2_Secret"

# CSS selectors for each frame text field
text_field_selector1 = "#input1"
text_field_selector2 = "#input2"

# CSS selectors for each frame Verify button
verify_button_selector1 = "button[onclick=\"verifyInput('input1')\"]"
verify_button_selector2 = "button[onclick=\"verifyInput('input2')\"]"

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:8000/dz.html")

def enter_text_frames(frame_name, secret_text, text_field_selector, verify_button_selector):
    """
    Switches into localhost iframe, enters the provided secret text,
    clicks the "Перевірити" button, handles the alert popup,
    checks the validation message, and then switches back
    to the default page context.

    Params;
        frame_name: name or id of the iframe to switch into
        secret_text: secret string to be entered into the input field
    """

    # 1. Switch into the frame
    driver.switch_to.frame(frame_name)

    # 2. Locate the input field and enter the secret value
    input_field = driver.find_element(By.CSS_SELECTOR, text_field_selector)
    input_field.clear()
    input_field.send_keys(secret_text)

    logging.info(f"Entered secret text for {frame_name}")

    # 3. Find and click the "Verify" button
    verify_button = driver.find_element(By.CSS_SELECTOR, verify_button_selector)
    verify_button.click()

    logging.info(f"Clicked verify button in {frame_name}")

    # 4. Handle alert message
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text

        logging.info(f"Alert from {frame_name}: {alert_text}")

        if alert_text == "Верифікація пройшла успішно!":
            logging.info(f"Validation passed in {frame_name}")
        elif alert_text == "Введено неправильний текст!":
            logging.error(f"Validation failed in {frame_name}")
        else:
            logging.warning(f"Unexpected alert message in {frame_name}: {alert_text}")

        alert.accept()
        logging.info(f"Alert accepted for {frame_name}")

    except NoAlertPresentException:
        logging.error(f"No alert appeared inside {frame_name}")

    # 5. Switch to default
    driver.switch_to.default_content()

    logging.info(f"Default content for {frame_name}")

enter_text_frames("frame1", SECRET_TEXT1, text_field_selector1, verify_button_selector1)
enter_text_frames("frame2", SECRET_TEXT2, text_field_selector2, verify_button_selector2)

driver.quit()

logging.info("All frames validated successfully!")

