import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_manager():

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "126.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser = Browser(Config(driver))

    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 4.0
    browser.config.type_by_js = True

    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--start-maximized')
    # driver_options.add_argument('--headless')

    browser.config.driver_options = driver_options

    yield browser

    browser.quit()