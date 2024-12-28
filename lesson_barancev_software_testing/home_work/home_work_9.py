'''
Сделайте сценарии, который на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
заходит в каждую из стран и проверяет, что зоны расположены в алфавитном порядке.
'''

from selenium import webdriver
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

geo_zones = driver.find_element(By.XPATH, '//*[@id="app-"]//span[text()="Geo Zones"]')
geo_zones.click()

cycle_country_row_count =len(driver.find_elements(By.XPATH, '//*[@class="row"]'))
x = 0

while x < cycle_country_row_count:
    country_list = driver.find_elements(By.XPATH, '//*[@id="content"]//tr//a[text()]')
    country_name = country_list[x].get_attribute('textContent')
    go_to_zone = country_list[x].get_attribute('href')
    driver.get(go_to_zone)

    zone_list = driver.find_elements(By.XPATH, '//*[@name="form_geo_zone"]//tbody//td[3]//option[.//@selected="selected"]')
    zone_list_string = []

    for i in zone_list:
        zone_list_string.append(i.get_attribute('textContent'))
    zone_list_string_sorted = sorted(zone_list_string)

    if zone_list_string_sorted == zone_list_string:
        print(f'Список регионов страны {country_name} отсортирован в алфавитном порядке' '\n')
        print(f'Список до сортировки {zone_list_string}' '\n')
        print(f'Список после сортировки {zone_list_string_sorted}' '\n')

    else:
        print(f'Список регионов страны {country_name} не отсортирован' '\n')
        print(f'Список до сортировки {zone_list_string}' '\n')
        print(f'Список после сортировки {zone_list_string_sorted}' '\n')

    geo_zones = driver.find_element(By.XPATH, '//*[@id="app-"]//span[text()="Geo Zones"]')
    geo_zones.click()
    x += 1

driver.quit()

