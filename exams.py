import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException


def login_user(student_id, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = ChromeService(executable_path="C:/WebDriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://staging.exams.prepdoctors.ca/")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "panel-body"))
        )

        student_id_input = driver.find_element(By.NAME, "loginName")
        student_id_input.send_keys(student_id)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        # Wait and check if the URL changes or some element of the landing appears
        WebDriverWait(driver, 10).until(
            EC.url_contains("landing")
        )

        # Check if login was successful
        if "landing" in driver.current_url:
            print(f"Login successful for {student_id}!")
            exams_table = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".examsListTable"))
            )
            start_button = driver.find_element(By.CSS_SELECTOR, ".examsListTable .start")
            driver.execute_script("arguments[0].scrollIntoView(true);", start_button)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".examsListTable .start"))
            )
            start_button.click()
            print(f"Clicked 'Start' for {student_id}!")

            # Wait for the SweetAlert popup to appear and click the confirmation button
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
            )
            confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm"))
            )
            confirm_button.click()
            print(f"Clicked 'Yes, start it!' for {student_id}!")

            answer_question(driver)



        else:
            print(f"Login failed for {student_id}.")
            driver.save_screenshot(f"{student_id}_login_failed.png")

    except Exception as e:
        print(f"An error occurred for {student_id}: {e}")
        driver.save_screenshot(f"{student_id}_error.png")

    finally:
        driver.quit()  # Ensure the driver is closed after the thread is done

def answer_question(driver):
    try:
        # Wait for the form to be visible
        form_visible = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "form"))
        )
        print("Form is visible.")

        # Check for labels associated with checkboxes
        labels = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox'] + label"))
        )

        print(f"Number of labels found: {len(labels)}")

        if labels:
            first_label = labels[2]
            first_label.click()
            print("Clicked the first checkbox label.")

            buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".qnav.btn.btn-primary.btn-xs"))
            )
            next_button = buttons[0]
            next_button.click()
            print("Clicked 'Next' button.")

            time.sleep(1)
            print("Waited for 1 seconds to view results.")

            labels = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox'] + label"))
             )

            submit = driver.find_element(By.CSS_SELECTOR, ".submit")
            submit.click()
            time.sleep(1)


            confirm_button = driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
            confirm_button.click()
            print(f"Clicked 'confirm'")


        else:
            print("No labels found.")

    except TimeoutException as e:
        print(f"Timeout occurred: {e}")
        print("Current URL:", driver.current_url)
        print("Page source:", driver.page_source)

    except Exception as e:
        print(f"An error occurred: {e}")


users = [
    ("6000000", "475692"),
    ("6000001", "662441"),
    ("6000002", "416615"),
    ("6000003", "399611"),
    ("6000004", "539616"),
    ("6000005", "947584"),
    ("6000006", "266428"),
    ("6000007", "627184"),
    ("6000008", "618969"),
    ("6000009", "139253"),
    ("6000010", "425721"),
    ("6000011", "467794"),
    ("6000012", "896492"),
    ("6000013", "813392"),
    ("6000014", "132991"),
    ("6000015", "667439"),
    ("6000016", "753654"),
    ("6000017", "435963"),
    ("6000018", "169945"),
    ("6000019", "496378"),
    ("6000020", "571742"),
    ("6000021", "723961"),
    ("6000022", "584516"),
    ("6000023", "497518"),
    ("6000024", "916612"),
    ("6000025", "862145"),
    ("6000026", "536154"),
    ("6000027", "314738"),
    ("6000028", "531671"),
    ("6000029", "273966"),
    ("6000030", "239516"),
    ("6000031", "679335"),
    ("6000032", "374285"),
    ("6000033", "693147"),
    ("6000034", "679562"),
    ("6000035", "317697"),
    ("6000036", "169833"),
    ("6000037", "731668"),
    ("6000038", "183277"),
    ("6000039", "572397"),
    ("6000040", "213547"),
    ("6000041", "773542"),
    ("6000042", "921517"),
    ("6000043", "382641"),
    ("6000044", "365944"),
    ("6000045", "516778"),
    ("6000046", "582744"),
    ("6000047", "724815"),
    ("6000048", "574528"),
    ("6000049", "796751"),
    ("6000050", "249778"),
    ("6549870", "564981"),
]


threads = []
for student_id, password in users:
    thread = threading.Thread(target=login_user, args=(student_id, password))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All login attempts and actions completed.")
