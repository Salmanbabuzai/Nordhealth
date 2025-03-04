from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page


    def open_login_page(self):
        self.page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def login_as_customer(self, customer_name: str):


    def login_as_manager(self):
