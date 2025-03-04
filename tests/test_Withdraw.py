from pages.Login_Page import LoginPage
from pages.Customer_Page import CustomerPage
from pytest import mark


@mark.order(5)
def test_withdraw_money(setup):
    page = setup
    login_page = LoginPage(page)
    customer_page = CustomerPage(page)
    login_page.login_as_customer("Genoa Dow")
    #customer_page.deposit_money("500")
    assert customer_page.withdraw_money("20") == "Transaction successful"
