from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# starting driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# go to the google site
driver.get("https://www.google.com")

# search for "Asimov Academy" text
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Asimov Academy")
search_box.submit()

# close the window
driver.quit()