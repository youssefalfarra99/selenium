from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

screen_sizes = [
    (320, 480),   # Mobile portrait
    (480, 800),   # Small tablet portrait
    (768, 1024),  # Tablet portrait
    (1024, 768),  # Tablet landscape
    (1440, 900),  # Laptop/desktop
    (1920, 1080)  # Full HD desktop
]

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    for size in screen_sizes:
        width, height = size
        driver.set_window_size(width, height)
        
        driver.get("https://prepdoctors.com")
        
        # Wait for 2 seconds before taking the screenshot
        time.sleep(2)
        
        screenshot_file = f"prepdoctors_{width}x{height}.png"
        driver.save_screenshot(screenshot_file)
        print(f"Screenshot captured for size {width}x{height}")

        if os.path.exists(screenshot_file):
            # Use JavaScript to get the inner width and height
            js_width = driver.execute_script("return window.innerWidth;")
            js_height = driver.execute_script("return window.innerHeight;")
            if js_width == width and js_height == height:
                print(f"Test Passed for size {width}x{height}")
            else:
                print(f"Test Failed for size {width}x{height}: Actual dimensions ({js_width}x{js_height}) do not match expected dimensions")
        else:
            print(f"Test Failed for size {width}x{height}: Screenshot file not found")

finally:
    driver.quit()
