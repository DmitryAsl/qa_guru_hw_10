import allure
from allure_commons.types import Severity
from helpers.steps import AllureSteps

issue_name = 'One piece'
issue_id = 94
repository = 'eroshenkoam/allure-example'

steps = AllureSteps()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "aslamov")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка созданной задачи в репозитории")
@allure.link("https://github.com", name="Testing")
def test_github_issue_name_steps():
    steps.open_github()
    steps.search_repository(repository)
    steps.go_to_repository(repository)
    steps.go_to_tab_issues()
    steps.assertion_issue_name_by_id(issue_id, issue_name)
