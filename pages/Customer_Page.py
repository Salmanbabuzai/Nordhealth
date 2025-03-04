import time

from playwright.sync_api import Page

class CustomerPage:
    def __init__(self, page: Page):
        self.page = page


    def verify_welcome_message(self):


    def deposit_money(self, amount: str):


    def withdraw_money(self, amount: str):


