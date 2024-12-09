'''
Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном приложении litecart.
Более точно, нужно открыть главную страницу, выбрать первый товар в блоке Campaigns и проверить следующее:
1) текстовое название товара одинаковые на главной странице и на странице товара - ОК
2) регулярная цена товара одинаковые на главной странице и на странице товара - ОК
3) акционная цена товара одинаковые на главной странице и на странице товара - ОК
4) регулярная цена ЗАЧЁРКНУТАЯ на главной странице - ОК
5) регулярная цена ЗАЧЁРКНУТАЯ на странице товара
6) регулярная цена СЕРОГО цвета на главной странице (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
7) регулярная цена СЕРОГО цвета на странице товара (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
8) акционная цена ЖИРНАЯ на главной странице
9) акционная цена ЖИРНАЯ на странице товара
10) акционная цена КРАСНОГО цвета на главной странице (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
11) акционная цена КРАСНОГО цвета на странице товара (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
12) акционная цена КРУПНЕЕ, чем обычная на главной странице
13) акционная цена КРУПНЕЕ, чем обычная на странице товара
14) кроссбраузерность - (Chrome, Firefox, IE)
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(2)

# нашли первую утку в блоке Кампейнс
first_campaigns_utka = driver.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]')

# нашли имя у найденной утки
name_main_page = first_campaigns_utka.find_element(By.XPATH, '//*[@id="box-campaigns"]/div/ul/li[1]/a[1]/div[2][text()]').text

# находим регулярную цену на главной странице
regular_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//s[text()]').text

# определяем тег регулярной цены на главной странице
crossout_regular_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//s').get_attribute('tagName')

# проверка №4 - регулярная цена зачёркнутая на главной странице
try:
    assert crossout_regular_price_main_page == 'S'
    print('Проверка №4 пройдена успешно')
except AssertionError:
    print('Упала проверка №4')

# определяем цвет регулярной цены на главной странице
color_regular_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//s[text()]').value_of_css_property('color')

# находим акционную цену на главной странице
campaign_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//strong[text()]').text

# определяем цвет акционной цены на главной странице
color_campaign_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//strong[text()]').value_of_css_property("color")

# переходим в карточку товара
first_campaigns_utka.click()

# находим название утки на странице карточки товара
name_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//h1').text

# проверка №1 - наименования товара одинаковые на обоих страницах
try:
    assert name_product_page == name_main_page
    print('Проверка №1 пройдена успешно')
except AssertionError:
    print('Упала проверка №1')

# находим регулярную цену на странице карточки товара
regular_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//s[@class="regular-price"]').text

# проверка №2 - регулярные цены товара одинаковые на обоих страницах
try:
    assert regular_price_product_page == regular_price_main_page
    print('Проверка №2 пройдена успешно')
except AssertionError:
    print('Упала проверка №2')


# находим акционную цену на странице карточки товара
campaign_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//strong[@class="campaign-price"]').text

# проверка №3 - акционные цены товара одинаковые на обоих страницах
try:
    assert campaign_price_product_page == campaign_price_main_page
    print('Проверка №3 пройдена успешно')
except AssertionError:
    print('Упала проверка №3')

# определяем тег регулярной цены на странице товара
crossout_regular_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//s').get_attribute('tagName')

# проверка №5 - регулярная цена зачёркнутая на странице товара
try:
    assert crossout_regular_price_product_page == 'S'
    print('Проверка №5 пройдена успешно')
except AssertionError:
    print('Упала проверка №5')





# time.sleep(5)
driver.quit()

