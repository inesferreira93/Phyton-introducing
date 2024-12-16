import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def initialize_browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=service, options=options)
    return driver

def capture_screenshot(driver, test_name):
    artifacts_dir = "artifacts"
    if os.path.exists(artifacts_dir):
        shutil.rmtree(artifacts_dir)
        print(f"Folder {artifacts_dir} removed.")
    
    os.makedirs(artifacts_dir)
    print(f"Folder {artifacts_dir} created.")
    
    screenshot_path = f"{artifacts_dir}/{test_name}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot captured: {screenshot_path}")

def pytest_configure():
    artifacts_dir = "artifacts"
    if os.path.exists(artifacts_dir):
        shutil.rmtree(artifacts_dir)
        print(f"Pasta {artifacts_dir} removida antes dos testes.")
    os.makedirs(artifacts_dir)
    print(f"Pasta {artifacts_dir} criada.")

