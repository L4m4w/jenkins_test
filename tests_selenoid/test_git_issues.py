import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s
from selenium import webdriver
# from conf.conf import browser_manager

def test_dynamic_steps():
    with allure.step('Open Git main page'):
        browser.config.base_url = 'https://github.com'
        browser.config.timeout = 4.0
        browser.config.type_by_js = True

        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('--start-maximized')
        # driver_options.add_argument('--headless')

        browser.config.driver_options = driver_options
        browser.open('/')

    with allure.step('Search for repo'):
        s(".header-search-button").click()
        s(".FormControl-input").send_keys('eroshenkoam/allure-example')
        s(".FormControl-input").submit()

    with allure.step('Redirect to repo'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Open the issues tab'):
        s("#issues-tab").click()

    with allure.step('Check issue number'):
        s(by.partial_text("#95")).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#95")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s(".FormControl-input").send_keys(repo)
    s(".FormControl-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()