import allure
from selene import by, have, be
from selene.support.shared.jquery_style import s
# from selenium import webdriver
# from conf import browser_manager


@allure.title("Successful fill form")
def test_successful(browser_manager):
    browser = browser_manager
    first_name = "Alex"
    last_name = "Egorov"

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element("#firstName").set_value(first_name)
        browser.element("#lastName").set_value(last_name)
        browser.element("#userEmail").set_value("alex@egorov.com")
        browser.element("#genterWrapper").element(by.text("Other")).click()
        browser.element("#userNumber").set_value("1231231230")
        # browser.element("#dateOfBirthInput").click()
        # browser.element(".react-datepicker__month-select").s("July")
        # browser.element(".react-datepicker__year-select").selectOption("2008")
        # browser.element(".react-datepicker__day--030:not(.react-datepicker__day--outside-month)").click()
        browser.element("#subjectsInput").send_keys("Maths")
        browser.element("#subjectsInput").press_enter()
        browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
        # browser.element("#uploadPicture").uploadFromClasspath("img/1.png")
        browser.element("#currentAddress").set_value("Some street 1")
        browser.element("#state").click()
        browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
        browser.element("#city").click()
        browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
        browser.element("#submit").click()

    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        # browser.element(".table-responsive").should(
        #     have.texts(first_name, last_name, "alex@egorov.com", "Some street 1"))

# def test_dynamic_steps(browser_manager):
#     browser = browser_manager
#     with allure.step('Open Git main page'):
#         browser.open('https://github.com/')
#
#     with allure.step('Search for repo'):
#         s(".header-search-button").click()
#         s(".FormControl-input").send_keys('eroshenkoam/allure-example')
#         s(".FormControl-input").submit()
#
#     with allure.step('Redirect to repo'):
#         s(by.link_text("eroshenkoam/allure-example")).click()
#
#     with allure.step('Open the issues tab'):
#         s("#issues-tab").click()
#
#     with allure.step('Check issue number'):
#         s(by.text("95")).should(be.visible)
#
# def test_decorator_steps(browser_manager):
#     browser = browser_manager
#     open_main_page(browser)
#     search_for_repository("eroshenkoam/allure-example")
#     go_to_repository("eroshenkoam/allure-example")
#     open_issue_tab()
#     should_see_issue_with_number("95")
#
#
# @allure.step("Открываем главную страницу")
# def open_main_page(browser):
#     browser.open("https://github.com")
#
#
# @allure.step("Ищем репозитория {repo}")
# def search_for_repository(repo):
#     s(".header-search-button").click()
#     s(".FormControl-input").send_keys(repo)
#     s(".FormControl-input").submit()
#
#
# @allure.step("Переходим по ссылке репозитория {repo}")
# def go_to_repository(repo):
#     s(by.link_text(repo)).click()
#
#
# @allure.step("Открываем таб Issues")
# def open_issue_tab():
#     s("#issues-tab").click()
#
#
# @allure.step("Проверяем наличие Issue с номером {number}")
# def should_see_issue_with_number(number):
#     s(by.text(number)).click()