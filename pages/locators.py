from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "input#id_login-username.form-control")
    PASSWORD = (By.CSS_SELECTOR, "input#id_login-password.form-control")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    PASSWORD_REGISTRATION_1 = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    PASSWORD_REGISTRATION_2 = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")
    BUTTON_LOG_IN = (By.NAME, "login_submit")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_THE_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    NAME_OF_THE_BOOK_IN_ALERT =(By.CSS_SELECTOR, "div.alertinner > strong")
    PRICE1 = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")

class BasketPageLocators:
    BOOK_TITLE = (By.CSS_SELECTOR, ".basket-items h3 a")
    BOOK_PRICE = (By.CSS_SELECTOR, ".basket-items .col-sm-1 .price_color")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")