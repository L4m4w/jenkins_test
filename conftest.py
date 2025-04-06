import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from selene import Browser, Config

from utils import attach

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://http://127.0.0.1:8080/wd/hub",
        options=options
    )

    browser.config.driver = driver

    # browser = Browser(Config(drive?r))
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()