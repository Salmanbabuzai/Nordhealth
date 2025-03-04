import time

from playwright.sync_api import Page

class CustomerPage:
    def __init__(self, page: Page):
        self.page = page
        self.welcome_message = page.locator(".fontBig")
        self.deposit_btn = page.locator('button[ng-click="deposit()"]')
        self.deposit_amount = page.locator("input[type='number']")
        self.deposit_submit = page.locator("button.btn.btn-default:has-text('Deposit')")
        self.withdraw_btn = page.locator("button[ng-click='withdrawl()']")
        self.withdraw_amount = page.locator("input[type='number']")
        self.withdraw_submit = page.locator("button.btn.btn-default:has-text('Withdraw')")
        self.success_message = page.locator(".error.ng-binding")

    def verify_welcome_message(self):
        return self.welcome_message.is_visible()

    def deposit_money(self, amount: str):
        self.deposit_btn.wait_for(state='visible')
        self.deposit_btn.click()
        self.deposit_amount.fill(amount)
        self.deposit_submit.click()
        return self.success_message.text_content()

    def withdraw_money(self, amount: str):
        self.withdraw_btn.click()
        self.withdraw_amount.fill(amount)
        self.withdraw_submit.click()
        return self.success_message.text_content()

