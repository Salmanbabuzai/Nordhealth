from pages.Login_Page import LoginPage
from pages.Manager_Page import ManagerPage
from pytest import mark


@mark.order(2)
def test_create_account(setup):
    page = setup
    login_page = LoginPage(page)
    manager_page = ManagerPage(page)
    login_page.login_as_manager()
    manager_page.create_account("Genoa Dow", "Dollar")

