from pages.Login_Page import LoginPage
from pages.Manager_Page import ManagerPage
from pytest import mark


@mark.order(1)
def test_add_customer(setup):
    page = setup
    login_page = LoginPage(page)
    manager_page = ManagerPage(page)
    login_page.login_as_manager()
    manager_page.add_customer("Genoa", "Dow", "16242")

