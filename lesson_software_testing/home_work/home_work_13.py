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

import random
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 2)

x = 0
while x < 5:
    quantity = int(driver.find_element(By.XPATH, '//span[@class="quantity"]').get_attribute('textContent'))
    utka = driver.find_element(By.XPATH, '//div//li[@class="product column shadow hover-light"][1]')
    utka.click()
    add_to_cart = driver.find_element(By.XPATH, '//button[@type="submit"][@name="add_cart_product"]')

    try:
        size_block = driver.find_element(By.XPATH, '//select[@name="options[Size]"]')
        size_block.click()
        choise_list = ["Small","Medium","Large"]
        choice_size = Select(size_block)                                                            # вариант 1 (выбор элемента из выпадающего списка)
        choice_size.select_by_value(random.choice(choise_list))                                     # вариант 1 (выбор элемента из выпадающего списка) + рандом
        # size = driver.find_element(By.XPATH, f'//option[@value="{random.choice(choise_list)}"]')  # вариант 2 (выбор элемента из выпадающего списка) + рандом
        # size.click()                                                                              # вариант 2 (выбор элемента из выпадающего списка)
    except NoSuchElementException:
        continue
    finally:
        order = int(driver.find_element(By.XPATH, '//input[@name="quantity"]').get_attribute('value'))
        quantity += order
        add_to_cart.click()
        wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//span[@class="quantity"]'), str(quantity)))
        driver.back()
        x += 1

go_to_cart = driver.find_element(By.XPATH, '//div[@id="cart"]//a[@class="link"]')
go_to_cart.click()

cart_row_list = driver.find_elements(By.XPATH, '//div[@id="box-checkout-summary"]//tbody//tr[.//td[@class="item"]]')
row_all = int(len(cart_row_list)) + 5

for i in range(len(cart_row_list)):
    remove = driver.find_element(By.XPATH, '//button[@value="Remove"]')
    remove.click()
    row_all -= 1
    wait.until(expected_conditions.invisibility_of_element((By.XPATH, f'//*[@id="order_confirmation-wrapper"]/table/tbody/tr[{row_all+1}]')))

driver.quit()