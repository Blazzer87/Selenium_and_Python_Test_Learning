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
from selenium.webdriver.common.devtools.v85.dom import get_attributes

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
country_list = driver.find_elements(By.XPATH, '//*[@id="content"]//form//a[text()]')
country_text_list = []

for n in range(len(country_list)):
    country_text_list.append(country_list[n].text)
country_text_list_sorted = sorted(country_text_list)
if country_text_list_sorted == country_text_list:
    print('Перечень стран отсортирован в алфавитном порядке')
else:
    print("Перечень стран не отсортирован")

geo = driver.find_element(By.XPATH, '//*[@class="row"][./td[6][text()=13]]/td[5]/a')
geo.click()

geozona_list = driver.find_elements(By.XPATH, '//*[@id="content"]/form/table/tbody/tr/td[6]')       # рабочий XPATH селектор, обращающийся к нужному элементу, но с постоянным значением
geozona_list_text = []

for m in range(len(geozona_list)):
    if int(geozona_list[m].text) >= 1:
        geozona_list_text.append(int(geozona_list[m].text))
        x = 0
        print(geozona_list_text[x])
        geo = driver.find_element(By.XPATH, '//*[@class="row"][./td[6][text()='f'{geozona_list_text[x]}]/td[5]/a')      # тот же самый рабочий XPATH селектор, но в который необходимо поместить элемент списка по индексу
        geo.click()
        x += 1


time.sleep(10)

driver.quit()


