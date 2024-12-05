'''
Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном приложении litecart.
Более точно, нужно открыть главную страницу, выбрать первый товар в блоке Campaigns и проверить следующее:
а) на главной странице и на странице товара совпадает текст названия товара
б) на главной странице и на странице товара совпадают цены (обычная и акционная)
в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
(цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)

Необходимо убедиться, что тесты работают в разных браузерах, желательно проверить во всех трёх ключевых браузерах (Chrome, Firefox, IE).
'''
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(2)

product_list = driver.find_elements(By.XPATH, '//*[@id="box-campaigns"]//*[@class="product column shadow hover-light"]')

main_product_name = driver.find_element(By.XPATH, '//*[@id="box-campaigns"]/div/ul/li[1]/a[1]/div[2][text()]')
print(main_product_name.text)
regular_price = driver.find_element(By.XPATH, '//*[@id="box-campaigns"]//*[@class="product column shadow hover-light"]//s[text()]')
print(regular_price.text)
campaign_price = driver.find_element(By.XPATH, '//*[@id="box-campaigns"]//*[@class="product column shadow hover-light"]//strong[text()]')
print(campaign_price.text)
color = campaign_price.value_of_css_property("color")
campaign_price = driver.find_element(By.XPATH, '//*[@id="box-campaigns"]//*[@class="product column shadow hover-light"]//strong[text()]').value_of_css_property('color')
print(color)
print(type(color))

#print(color.text)
#regular_price_not relevant = driver.find_element(By.XPATH,




product_list[0].click()



time.sleep(5)
driver.quit()

