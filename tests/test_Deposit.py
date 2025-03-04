from pages.Login_Page import LoginPage
from pages.Customer_Page import CustomerPage
from pytest import mark


@mark.order(4)
def test_deposit_money(setup):
    page = setup
    login_page = LoginPage(page)
    customer_page = CustomerPage(page)
    login_page.login_as_customer("Genoa Dow")
    assert customer_page.deposit_money("500") == "Deposit Successful"