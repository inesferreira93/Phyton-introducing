import os
import pytest
import shutil
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
        print(f"Test {item.nodeid} falhou. Tentando capturar screenshot.")
        if "browser" in item.funcargs:
            try:
                driver = item.funcargs["browser"]
                capture_screenshot(driver, item.nodeid.replace("::", "_"))
                print(f"Screenshot capturada para o teste: {item.nodeid}")
            except Exception as e:
                print(f"Erro ao capturar screenshot: {e}")

def pytest_configure():
    artifacts_dir = "artifacts"
    if os.path.exists(artifacts_dir):
        shutil.rmtree(artifacts_dir)
        print(f"Folder {artifacts_dir} was removed before the tests.")
    os.makedirs(artifacts_dir)
    print(f"Folder {artifacts_dir} created.")
