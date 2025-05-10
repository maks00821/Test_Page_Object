import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

    time.sleep(10)

@pytest.mark.login_guest
class TestLoginFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.link = "https://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.browser = browser  # если нужно напрямую

    def test_guest_can_go_to_login_page_from_product_page(self):
        self.page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self):
        self.page.should_be_login_link()