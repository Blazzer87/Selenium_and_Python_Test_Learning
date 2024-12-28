import os

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
options.add_argument('incognito')                   # передаём инкогнито в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

def is_element_present(driver, locator):
    return len(driver.find_elements(locator))>0

driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog')
driver.implicitly_wait(2)

username = driver.find_element(By.CSS_SELECTOR, '[name=username]')
username.send_keys('admin')
password = driver.find_element(By.CSS_SELECTOR, '[name=password]')
password.send_keys('admin')
rememberme = driver.find_element(By.CSS_SELECTOR, '[name=remember_me]')
rememberme.click()
submit = driver.find_element(By.CSS_SELECTOR, '[name=login]')
submit.click()

print(is_element_present(driver,'//a[contains(@class,"button")][text()=" Add New Product"]'))




# add_new_product = driver.find_element(By.XPATH, '//a[contains(@class,"button")][text()=" Add New Product"]')
# add_new_product.click()