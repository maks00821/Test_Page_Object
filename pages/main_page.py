from .base_page import BasePage
from .login_page import LoginPage
import pytest


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


