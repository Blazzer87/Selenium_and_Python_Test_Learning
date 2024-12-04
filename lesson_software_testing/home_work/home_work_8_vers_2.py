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
print('\n')

row_zones_list = driver.find_elements(By.XPATH, '//*[@id="content"]/form/table/tbody/tr/td[6]')
row_countries_list = driver.find_elements(By.XPATH, '//*[@id="content"]/form/table/tbody/tr/td[5]/a')
y = 0
row_zones_list_int = []
row_html_list = []
zones_list_str = []

for i in range(len(row_zones_list)):
    row_zones_list_int.append(int(row_zones_list[i].text))
    row_html_list.append(row_countries_list[i].get_attribute('href'))

for m in range(len(row_zones_list_int)):
    if row_zones_list_int[m] >= 1:
        driver.get(row_html_list[m])
        zones_list = driver.find_elements(By.XPATH, '//*[@id="table-zones"]/tbody/tr/td[3][.//text()]')
        for k in zones_list:
            zones_list_str.append(k.get_attribute('textContent'))
            zones_list_str_sorted = sorted(zones_list_str)
        country = driver.find_element(By.XPATH, '//*[@id="content"]/form/table[1]/tbody/tr[4]/td/input')
        country_name = country.get_attribute('value')
        if zones_list_str_sorted == zones_list_str:
            print(f'Список регионов страны {country_name} отсортирован в алфавитном порядке')
            print(f'Список без сортировки {zones_list_str}')
            print(f'Список с сортировкой {zones_list_str_sorted}')
        else:
            print(f'Список регионов страны {country_name} не отсортирован')
            print(f'Список без сортировки {zones_list_str}')
            print(f'Список с сортировкой {zones_list_str_sorted}')
        print('\n')

driver.quit()

