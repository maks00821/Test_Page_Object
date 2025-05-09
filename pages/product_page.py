from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.remote.webelement import WebElement

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button: WebElement = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def get_product_name(self):
        product_name_element: WebElement = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_BOOK)
        return product_name_element.text

    def get_product_price(self):
        product_price_element: WebElement = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        return product_price_element.text

    def should_be_product_added_message(self, expected_name, expected_price):
        self.should_be_correct_product_name_in_message(expected_name)
        self.should_be_correct_product_price_in_message(expected_price)

    def should_be_correct_product_name_in_message(self, expected_name):
        message_name_element: WebElement = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_BOOK_IN_ALERT)
        assert expected_name == message_name_element.text, f"Ожидаемое название товара '{expected_name}' не совпадает с названием в сообщении '{message_name_element.text}'"

    def should_be_correct_product_price_in_message(self, expected_price):
        message_price_element: WebElement = self.browser.find_element(*ProductPageLocators.PRICE1)
        assert expected_price in message_price_element.text, f"Ожидаемая цена '{expected_price}' не найдена в сообщении о цене '{message_price_element.text}'"