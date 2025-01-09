from selene import by, have, browser

issue_name = 'One piece'


def test_github_issue_name():
    browser.open('https://github.com')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('[data-content="Issues"]').click()

    browser.element('#issue_94_link').should(have.text(issue_name))
