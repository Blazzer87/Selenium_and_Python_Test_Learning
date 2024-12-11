"""Сделайте сценарий, который проверяет, что ссылки на странице редактирования страны открываются в новом окне.
Сценарий должен состоять из следующих частей:
1) зайти в админку
2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
3) открыть на редактирование какую-нибудь страну или начать создание новой
4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой -
- они ведут на внешние страницы и открываются в новом окне, именно это и нужно проверить.
Конечно, можно просто убедиться в том, что у ссылки есть атрибут target="_blank".
Но в этом упражнении требуется именно кликнуть по ссылке, чтобы она открылась в новом окне,
потом переключиться в новое окно, закрыть его, вернуться обратно, и повторить эти действия для всех таких ссылок.
Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна."""

import time
import random

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
options.add_argument('incognito')                   # передаём инкогнито в опции хрома
options.add_argument('incognito')                   # передаём инкогнито в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
driver.implicitly_wait(2)

username = driver.find_element(By.CSS_SELECTOR, '[name=username]')
username.send_keys('admin')
password = driver.find_element(By.CSS_SELECTOR, '[name=password]')
password.send_keys('admin')
rememberme = driver.find_element(By.CSS_SELECTOR, '[name=remember_me]')
rememberme.click()
submit = driver.find_element(By.CSS_SELECTOR, '[name=login]')
submit.click()

edit_country_list = driver.find_elements(By.XPATH, '//a[@title="Edit"]')
random_edit_country = random.choice(edit_country_list)
random_edit_country.click()

link_button_list = driver.find_elements(By.XPATH, '//form[@method="post"]//a[@target="_blank"]')

elements_locator_dict = {
    'iso_code_2':'//td[./input[@name="iso_code_2"]]/a[@target="_blank"]',
    'iso_code_3':'//td[./input[@name="iso_code_3"]]/a[@target="_blank"]',
    'tax_id_format':'//td[./input[@name="tax_id_format"]]/a[@target="_blank"]',
    'address_format':'//td[./textarea[@name="address_format"]]/a[@target="_blank"]',
    'postcode_format':'//td[./input[@name="postcode_format"]]/a[@target="_blank"]',
    'currency_code':'//td[./input[@name="currency_code"]]/a[@target="_blank"]',
    'phone_code':'//td[./input[@name="phone_code"]]/a[@target="_blank"]'
}

main_window = driver.current_window_handle

for i in range(len(link_button_list)):
    link = driver.find_element(By.XPATH, f'{list(elements_locator_dict.values())[i]}')
    link.click()
    wait = WebDriverWait(driver, 2)
    wait.until(expected_conditions.number_of_windows_to_be(2))
    all_window_list = driver.window_handles
    for window_for_open_link in all_window_list:
        if window_for_open_link != main_window:
            driver.switch_to.window(window_for_open_link)
            all_window_list.remove(window_for_open_link)
            break
    try:
        driver.set_page_load_timeout(10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//h1')))
    except TimeoutException:
        continue
    finally:
        h1 = driver.find_element(By.XPATH, '//h1')
        print(f"Успешно открыта страница {h1.text}.")
        driver.close()
        driver.switch_to.window(main_window)
print("Проверка завершена.")
driver.quit()
