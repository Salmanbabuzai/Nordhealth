from playwright.sync_api import Page

class ManagerPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_customer_btn = page.locator("button[ng-class='btnClass1']")
        self.open_account_btn = page.locator("button:has-text('Open Account')")
        self.first_name_input = page.locator("input[placeholder='First Name']")
        self.last_name_input = page.locator("input[placeholder='Last Name']")
        self.post_code_input = page.locator("input[placeholder='Post Code']")
        self.add_customer_submit = page.locator("button.btn.btn-default:has-text('Add Customer')")
        self.customer_dropdown = page.locator("#userSelect")
        self.currency_dropdown = page.locator("#currency")
        self.process_btn = page.locator("button:has-text('Process')")

    def add_customer(self, first_name, last_name, post_code):
        self.add_customer_btn.click()
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.post_code_input.fill(post_code)
        self.add_customer_submit.click()
        #self.page.on("dialog", lambda dialog: dialog.accept())

    def create_account(self, customer_name, currency):
        self.open_account_btn.click()
        self.customer_dropdown.select_option(label=customer_name)
        self.currency_dropdown.select_option(label=currency)
        self.process_btn.click()
        #self.page.on("dialog", lambda dialog: dialog.accept())
