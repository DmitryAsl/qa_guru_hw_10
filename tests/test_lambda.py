from selene import by, have, browser
import allure

issue_name = 'One piece'


def test_github_issue_name_lambda():
    with allure.step("Открываем сайт"):
        browser.open('https://github.com')
    with allure.step("Открываем нужный репозторий"):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step("Переходим на таб Issue"):
        browser.element('[data-content="Issues"]').click()
    with allure.step("Проверяем название Issue"):
        browser.element('#issue_94_link').should(have.text(issue_name))
