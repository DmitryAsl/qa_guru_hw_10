from selene import by, have, browser

import allure


class AllureSteps:
    @allure.step("Открываем сайт")
    def open_github(self):
        browser.open('https://github.com')

    @allure.step("Ищем репозиторий {repo}")
    def search_repository(self, repo: str):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys(repo).press_enter()

    @allure.step("Открываем репозиторий {repo}")
    def go_to_repository(self, repo: str):
        browser.element(by.link_text(repo)).click()

    @allure.step("Переходим на таб Issue")
    def go_to_tab_issues(self):
        browser.element('[data-content="Issues"]').click()

    @allure.step("Проверяем название Issue - {name}")
    def assertion_issue_name_by_id(self, id_issue, name: str):
        browser.element(f'#issue_{id_issue}_link').should(have.text(name))
