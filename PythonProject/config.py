import os
import pytest
from utils.browser import initialize_browser, capture_screenshot

@pytest.fixture
def browser():
    driver = initialize_browser()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Verifica se o teste falhou
    if rep.when == "call" and rep.failed:
        print(f"Test {item.nodeid} falhou. Tentando capturar screenshot.")
        if "browser" in item.funcargs:
            driver = item.funcargs["browser"]
            capture_screenshot(driver, item.nodeid.replace("::", "_"))

