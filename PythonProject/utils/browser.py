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
    
    driver = webdriver.Chrome(service=service, options=options)
    return driver
