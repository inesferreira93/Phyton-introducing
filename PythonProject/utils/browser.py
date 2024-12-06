from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def initialize_browser():
    # Use o WebDriverManager para configurar o caminho correto do ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    
    # Inicializa o WebDriver com o caminho do driver e as opções
    driver = webdriver.Chrome(service=service, options=options)
    return driver
