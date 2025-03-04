from pages.Login_Page import LoginPage
from pages.Customer_Page import CustomerPage
from pytest import mark
from playwright.sync_api import expect

@mark.order(3)
def test_login_as_customer(setup):
    page = setup
    login_page = LoginPage(page)
    customer_page = CustomerPage(page)
    login_page.login_as_customer("Genoa Dow")

    expect(customer_page.welcome_message).to_be_visible()

    assert customer_page.verify_welcome_message()
