import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

ADMIN_LOGIN = 'user'
ADMIN_PASSWORD = 'bitnami'


def login_to_admin(driver, base_url):
    driver.get(base_url + '/administration/')
    input_username = driver.find_element(By.ID, 'input-username')
    input_password = driver.find_element(By.ID, 'input-password')
    input_username.send_keys(ADMIN_LOGIN)
    input_password.send_keys(ADMIN_PASSWORD)
    driver.find_element(By.ID, 'form-login').find_element(By.TAG_NAME, 'button').click()
    WebDriverWait(driver, 2).until(EC.title_contains('Dashboard'))


@allure.feature('Тестирование административной панели')
@allure.story('Тестирование авторизации')
def test_admin_login(driver, base_url):
    login_to_admin(driver, base_url)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Dashboard'


@allure.story('Тестирование получения API-токена')
def test_get_api_token(driver, base_url):
    login_to_admin(driver, base_url)
    url = driver.find_element(By.ID, 'collapse-7-1').find_elements(By.TAG_NAME, 'a')[2].get_attribute('href')
    driver.get(url)
    driver.find_element(By.XPATH,
                        '//body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/a[1]').click()
    prev_token = driver.find_element(By.ID, 'input-key').text
    driver.find_element(By.ID, 'button-generate').click()
    driver.find_element(By.XPATH, '//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]').click()
    driver.find_element(By.XPATH, '//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]').click()
    driver.find_element(By.XPATH,
                        '//body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/a[1]').click()
    new_token = driver.find_element(By.ID, 'input-key').text
    assert prev_token != new_token and len(new_token) == 256




