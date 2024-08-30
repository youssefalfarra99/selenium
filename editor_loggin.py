from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver (e.g., Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximize the browser window on start
service = ChromeService(executable_path="C:/WebDriver/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

# Open the WordPress login page and log in
driver.get('https://prepdoctors.com/wp-login.php')

# Wait for the username input field to be visible
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'user_login')))
username_input.send_keys('youssef.alfarra')

# Find and enter password
password_input = driver.find_element(By.ID, 'user_pass')
password_input.send_keys('mrkIYHJDL1vggVUXoKGnEUc8HczkJW')

# Find and click login button
login_button = driver.find_element(By.ID, 'wp-submit')
login_button.click()

# Wait for the dashboard to load
dashboard_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.wp-menu-name')))
dashboard_link.click()

# Navigate to Posts > Add New
driver.get('https://prepdoctors.com/wp-admin/post-new.php')

# Wait for the title input field to be visible
title_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'title')))
title_input.send_keys('Automated Post Title')

# Find and enter content
content_input = driver.find_element(By.ID, 'content')
content_input.send_keys('This is the content of the automated post.')

# Find and click publish button
publish_button = driver.find_element(By.ID, 'publish')
publish_button.click()

# Wait for the post to be published
publish_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'message')))
print(publish_message.text)

# Clean up and close the browser
driver.quit()
