import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def setup(context):
    page = context.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    yield page
    page.close()
