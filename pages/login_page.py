from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Подстрока 'login' не найдена в URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN), "Поле LOGIN не найдено"
        assert self.is_element_present(*LoginPageLocators.PASSWORD), "Поле PASSWORD не найдено"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION), "Поле EMAIL_REGISTRATION не найдено"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_1), "Поле PASSWORD_REGISTRATION_1 не найдено"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_2), "Поле PASSWORD_REGISTRATION_2 не найдено"