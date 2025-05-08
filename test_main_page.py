from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage



def test_open_language_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


    time.sleep(10)