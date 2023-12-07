import time

from selenium.webdriver.common.by import By
import allure


@allure.feature('Тестирование навигации')
@allure.story('Тестирование главного меню')
def test_main_menu_navigation(driver, base_url):
    driver.get(base_url)
    num = len(driver.find_elements(By.CLASS_NAME, 'nav-item'))
    for i in range(num):
        driver.find_elements(By.CLASS_NAME, 'nav-item')[i].click()
        try:
            driver.find_elements(By.CLASS_NAME, 'nav-item')[i].find_element(By.CLASS_NAME, 'see-all').click()
        except Exception:
            driver.find_element(By.ID, 'logo').click()


@allure.story('Тестирование карточек продукта')
def test_product_cards_navigation(driver, base_url):
    driver.get(base_url)
    num = len(driver.find_elements(By.CLASS_NAME, 'product-thumb'))
    for i in range(num):
        product = driver.find_elements(By.CLASS_NAME, 'product-thumb')[i].find_element(By.TAG_NAME, 'h4').text
        driver.find_elements(By.CLASS_NAME, 'product-thumb')[i].find_element(By.TAG_NAME, 'a').click()
        assert driver.find_element(By.TAG_NAME, 'h1').text == product
        driver.find_element(By.ID, 'logo').click()


@allure.story('Тестирование смены валюты')
def test_currency_change(driver, base_url):
    driver.get(base_url)
    num = len(driver.find_element(By.ID, 'form-currency').find_element(By.CLASS_NAME, 'dropdown-menu').find_elements(
        By.TAG_NAME, 'a'))
    for i in range(num):
        driver.find_element(By.CLASS_NAME, 'dropdown-toggle').click()
        form_currency = driver.find_element(By.ID, 'form-currency')
        currency = form_currency.find_element(By.CLASS_NAME, 'dropdown-menu').find_elements(By.TAG_NAME, 'a')[i].text[0]
        form_currency.find_element(By.CLASS_NAME, 'dropdown-menu').find_elements(By.TAG_NAME, 'a')[i].click()
        assert currency == driver.find_element(By.ID, 'form-currency').find_element(By.TAG_NAME, 'strong').text
