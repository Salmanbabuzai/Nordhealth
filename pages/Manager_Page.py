from playwright.sync_api import Page

class ManagerPage:
    def __init__(self, page: Page):
        self.page = page


    def add_customer(self, first_name, last_name, post_code):


    def create_account(self, customer_name, currency):

