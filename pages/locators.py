from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "input#id_login-username.form-control")
    PASSWORD = (By.CSS_SELECTOR, "input#id_login-password.form-control")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    PASSWORD_REGISTRATION_1 = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    PASSWORD_REGISTRATION_2 = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")