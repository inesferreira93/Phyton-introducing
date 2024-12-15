from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    CONCENTBANNER = (By.XPATH, "//button[contains(@class, 'fc-cta-consent')]")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    ADDRESS = (By.XPATH, "//textarea[@ng-model='Adress']")
    EMAIL = (By.XPATH, "//input[@type='email']")
    PHONE = (By.XPATH, "//input[@type='tel']")
    GENDER_MALE = (By.XPATH, "//input[@value='Male']")
    HOBBIES_MOVIES = (By.ID, "checkbox2")
    LANGUAGES = (By.ID, "msdd")
    SKILL_DROPDOWN = (By.ID, "Skills")
    SUBMIT_BUTTON = (By.ID, "submitbtn")

    # Métodos para interagir com a página
    def accept_user_concents(self):
        self.driver.find_element(*self.CONCENTBANNER).click()

    def fill_form(self, first_name, last_name, address, email, phone):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PHONE).send_keys(phone)

    def select_gender(self):
        self.driver.find_element(*self.GENDER_MALE).click()

    def select_hobby(self):
        self.driver.find_element(*self.HOBBIES_MOVIES).click()

    def select_skill(self, skill):
        dropdown = Select(self.driver.find_element(*self.SKILL_DROPDOWN))
        dropdown.select_by_visible_text(skill)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
