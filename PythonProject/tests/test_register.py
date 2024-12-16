from utils.browser import initialize_browser
from pages.register_page import RegisterPage

def test_fill_form():
    # Usando a função de inicialização do WebDriver
    browser = initialize_browser()
    browser.get("https://demo.automationtesting.in/Register.html")
    
    register_page = RegisterPage(browser)
    register_page.accept_user_concents()
    register_page.fill_form()
    
    browser.quit()
