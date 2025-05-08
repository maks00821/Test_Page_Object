from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_open_language_page(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button is not None, "Кнопка корзины не найдена"

    time.sleep(30)