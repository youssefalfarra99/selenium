from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://prepdoctors.com")
    initial_url = driver.current_url
    print(f"Initial URL: {initial_url}")

    journey_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Choose your Journey"))
    )
    journey_button = driver.find_element(By.ID, 'text-click')

    journey_button.click()

    try:
        WebDriverWait(driver, 20).until(lambda d: d.current_url != initial_url)
    except Exception as e:
        print(f"Exception while waiting for URL to change: {str(e)}")

    new_url = driver.current_url
    print(f"New URL: {new_url}")

    if initial_url == new_url:
        print("Test Failed: The page refreshed and the URL did not change.")
    else:
        print("Test Passed: The page refreshed when the 'Choose Your Journey' button was clicked.")
    
finally:
    driver.quit()
