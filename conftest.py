import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selene.support.shared import browser
from utils import attach


@pytest.fixture(scope='function')
def browser_manager(request):

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    attach.add_html(browser)

    browser.quit()