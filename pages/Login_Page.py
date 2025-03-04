from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.customer_login_btn = page.locator("button:has-text('Customer Login')")
        self.manager_login_btn = page.locator("button:has-text('Bank Manager Login')")
        self.user_dropdown = page.locator("#userSelect")
        self.login_btn = page.locator("button:has-text('Login')")

    def open_login_page(self):
        self.page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def login_as_customer(self, customer_name: str):
        self.customer_login_btn.click()
        self.user_dropdown.select_option(label=customer_name)
        self.login_btn.click()

    def login_as_manager(self):
        self.manager_login_btn.click()