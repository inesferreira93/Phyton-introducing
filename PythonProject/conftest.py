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

    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("screenshot_failures.log") else "w"
        with open("screenshot_failures.log", mode) as f:
            if "browser" in item.funcargs:
                driver = item.funcargs["browser"]
                screenshot_path = f"screenshots/{item.nodeid.replace('::', '_')}.png"
                capture_screenshot(driver, item.nodeid.replace("::", "_"))
                f.write(f"Screenshot captured: {screenshot_path}\n")
