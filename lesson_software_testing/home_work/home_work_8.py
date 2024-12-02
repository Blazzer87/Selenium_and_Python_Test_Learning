'''
Сделайте сценарий для учебного приложения litecart,
который на странице http://localhost/litecart/admin/?app=countries&doc=countries
а) проверяет, что страны расположены в алфавитном порядке
б) для тех стран, у которых количество зон отлично от нуля -- открывает страницу
этой страны и там проверяет, что геозоны расположены в алфавитном порядке
'''
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/admin/login.php')
driver.implicitly_wait(2)

username = driver.find_element(By.CSS_SELECTOR, '[name=username]')
username.send_keys('admin')
password = driver.find_element(By.CSS_SELECTOR, '[name=password]')
password.send_keys('admin')
rememberme = driver.find_element(By.CSS_SELECTOR, '[name=remember_me]')
rememberme.click()
submit = driver.find_element(By.CSS_SELECTOR, '[name=login]')
submit.click()

countries = driver.find_element(By.XPATH, '//*[@id="app-"]//span[text()="Countries"]')
countries.click()



time.sleep(2)

driver.quit()


