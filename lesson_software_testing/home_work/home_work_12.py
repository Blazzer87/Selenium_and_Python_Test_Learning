"""Сделайте сценарий для добавления нового товара (продукта) в учебном приложении litecart (в админке).
Для добавления товара нужно открыть меню Catalog, в правом верхнем углу нажать кнопку "Add New Product",
заполнить поля с информацией о товаре и сохранить.
Достаточно заполнить только информацию на вкладках General, Information и Prices.
Скидки (Campains) на вкладке Prices можно не добавлять.
Картинку с изображением товара нужно уложить в репозиторий вместе с кодом.
Надо средствами языка программирования преобразовать относительный путь в абсолютный.
После сохранения товара нужно убедиться, что он появился в каталоге (в админке).
Клиентскую часть магазина можно не проверять."""
import os

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
options.add_argument('incognito')                   # передаём инкогнито в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

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

utka_name = "test_utka_pank"

add_new_product = driver.find_element(By.XPATH, '//a[contains(@class,"button")][text()=" Add New Product"]')
add_new_product.click()

status_enabled = driver.find_element(By.XPATH, '//label[.//@value="1"]')
status_enabled.click()

name_product = driver.find_element(By.XPATH, '//input[@name="name[en]"]')
name_product.send_keys(f'{utka_name}')

code_product = driver.find_element(By.XPATH, '//input[@name="code"]')
code_product.send_keys('какой-то код')

categories_rubber_ducks = driver.find_element(By.XPATH, '//input[@type="checkbox"][@data-name="Rubber Ducks"]')
categories_rubber_ducks.click()

categories_subcategory = driver.find_element(By.XPATH, '//input[@type="checkbox"][@data-name="Subcategory"]')
categories_subcategory.click()

default_category = driver.find_element(By.XPATH, '//option[text()="Subcategory"]')
default_category.click()

unisex_gender_checkbox = driver.find_element(By.XPATH, '//input[@type="checkbox"][@value="1-3"]')
unisex_gender_checkbox.click()

quantity_input = driver.find_element(By.XPATH, '//input[@name="quantity"]')
quantity_input.clear()
quantity_input.send_keys('25')


upload_images = driver.find_element(By.XPATH, '//input[@type="file"][@name="new_images[]"]')
relative_path_image = 'utkapank.jpg'
absolute_path_image = os.path.abspath(relative_path_image)
upload_images.send_keys(absolute_path_image)

data_valid_from = driver.find_element(By.XPATH, '//input[@type="date"][@name="date_valid_from"]')
data_valid_from.send_keys('09122024')

data_valid_to = driver.find_element(By.XPATH, '//input[@type="date"][@name="date_valid_to"]')
data_valid_to.send_keys('31122025')

information = driver.find_element(By.XPATH, '//a[text()="Information"]')
information.click()

manufacture = driver.find_element(By.XPATH, '//select[@name="manufacturer_id"]')
manufacture.click()

acme = driver.find_element(By.XPATH, '//select[@name="manufacturer_id"]//option[@value="1"]')
acme.click()

keywords = driver.find_element(By.XPATH, '//input[@type="text"][@name="keywords"]')
keywords.send_keys('utka keywords')

short_description = driver.find_element(By.XPATH, '//input[@type="text"][@name="short_description[en]"]')
short_description.send_keys('utka short description')

description = driver.find_element(By.XPATH, '//div[@class="trumbowyg-editor"]')
description.send_keys('utka description')

head_title = driver.find_element(By.XPATH, '//input[@type="text"][@name="head_title[en]"]')
head_title.send_keys('utka head title')

meta_description = driver.find_element(By.XPATH, '//input[@type="text"][@name="meta_description[en]"]')
meta_description.send_keys('utka meta description')

prices = driver.find_element(By.XPATH, '//a[text()="Prices"]')
prices.click()

purchase_price = driver.find_element(By.XPATH, '//input[@name="purchase_price"]')
purchase_price.clear()
purchase_price.send_keys('48')

purchase_price_currency_code = driver.find_element(By.XPATH, '//select[@name="purchase_price_currency_code"]')
purchase_price_currency_code.click()
currency_code = driver.find_element(By.XPATH, '//option[@value="USD"]')
currency_code.click()

price_usd = driver.find_element(By.XPATH, '//input[@type="text"][@name="prices[USD]"]')
price_usd.clear()
price_usd.send_keys('45')

price_euro = driver.find_element(By.XPATH, '//input[@type="text"][@name="prices[EUR]"]')
price_euro.clear()
price_euro.send_keys('40')

save_button = driver.find_element(By.XPATH, '//button[@type="submit"][@name="save"]')
save_button.click()

catalog_list_1 = driver.find_element(By.XPATH, '//a[text()="Rubber Ducks"]')
catalog_list_1.click()

catalog_list_2 = driver.find_element(By.XPATH, '//a[text()="Subcategory"]')
catalog_list_2.click()

try:
    utka_pank = driver.find_element(By.XPATH, f'//a[text()="{utka_name}"]')
    print("Новый товар добавлен в каталог")
except NoSuchElementException:
    print("Товар утка панк не добавлена в каталог")

driver.quit()