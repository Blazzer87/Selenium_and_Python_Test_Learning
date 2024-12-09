"""
Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
1) открыть главную страницу
2) открыть первый товар из списка
2) добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
3) подождать, пока счётчик товаров в корзине обновится
4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(2)

x = 0
while x < 3:
    utka = driver.find_element(By.XPATH, '//div//li[@class="product column shadow hover-light"][1]')
    utka.click()
    add_to_cart = driver.find_element(By.XPATH, '//button[@type="submit"][@name="add_cart_product"]')
    add_to_cart.click()
    x += 1
    driver.back()

cart = driver.find_element(By.XPATH, '//div[@id="cart"]//a[@class="link"]')
cart.click()

cart_list = driver.find_elements(By.XPATH, '//li[@class="shortcut"]')

for i in range(len(cart_list)):
    utka_cart = driver.find_element(By.XPATH, '//li[@class="shortcut"]//a[@class="inact act"]')
    utka_cart.click()
    remove = driver.find_element(By.XPATH, '//button[@value="Remove"]')
    remove.click()

time.sleep(5)
driver.quit()