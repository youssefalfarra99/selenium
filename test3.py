from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.service import Service as SafariService
import time

def test_website_in_browsers():
    chrome_driver = ie_driver = edge_driver = safari_driver = None
    try:
        print("Testing in Chrome...")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=chrome_options)
        test_website(chrome_driver, "Chrome")

        # print("Testing in Internet Explorer...")
        # ie_driver = webdriver.Ie(service=webdriver.ie.service.Service(IEDriverManager().install()))
        # test_website(ie_driver, "Internet Explorer")

        print("Testing in Microsoft Edge...")
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
        test_website(edge_driver, "Microsoft Edge")

        # print("Testing in Safari...")
        # safari_driver = webdriver.Safari(service=SafariService())
        # test_website(safari_driver, "Safari")

    except Exception as ex:
        print(f"Exception occurred: {str(ex)}")

    finally:
        if chrome_driver:
            chrome_driver.quit()
        # if ie_driver:
        #     ie_driver.quit()
        if edge_driver:
            edge_driver.quit()
        # if safari_driver:
        #     safari_driver.quit()

def test_website(driver, browser_name):
    if driver:
        try:
            print(f"Opening website in {browser_name}...")
            driver.get("https://prepdoctors.com")
            time.sleep(2) 
            current_url = driver.current_url
            if "prepdoctors.com" in current_url:
                print(f"{browser_name}: Website opened successfully")
            else:
                print(f"{browser_name}: Failed to open website")
        except Exception as ex:
            print(f"Exception occurred while testing {browser_name}: {str(ex)}")

test_website_in_browsers()
