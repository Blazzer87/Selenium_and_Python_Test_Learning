import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём в опции хрома, что он запуститься во весь экран

driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/admin/login.php')

def find_and_send_keys (input, locator):
    field = driver.find_element(By.XPATH, f'{locator}')
    field.clear()
    field.send_keys(f'{input}')

def find_and_click (locator):
    tab = driver.find_element(By.XPATH, f'{locator}')
    tab.click()

find_and_send_keys('admin', '//input[@name="username"]')
find_and_send_keys('admin', '//input[@name="password"]')
find_and_click('//input[@type="checkbox"]')
find_and_click('//button[@type="submit"][@name="login"]')

driver.quit()