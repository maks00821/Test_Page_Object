from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert "basket" in self.browser.current_url, "Подстрока 'basket' не найдена в URL"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), f"Корзина не пустая"