from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# starting driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# go to the google site
driver.get("https://demo.automationtesting.in/Register.html")

# accepts the concent banner
concentButton = driver.find_element(By.XPATH, "//button[contains(@class, 'fc-cta-consent')]")
concentButton.click()

# search for "Asimov Academy" text
firstName = driver.find_element(By.XPATH, "//input[@ng-model='FirstName']")
firstName.click()
firstName.send_keys("MyFirstName")

lastName = driver.find_element(By.XPATH, "//input[@ng-model='LastName']")
lastName.click()
lastName.send_keys("MyLastName")

addressInput = driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
addressInput.click()
addressInput.send_keys("My address in Portugal is secret")

# close the window
#driver.quit()