"""Установите какой-нибудь прокси-сервер, который умеет протоколировать запросы и ответы.
На выбор прокси-сервера для разных платформ:
http://www.telerik.com/fiddler (Windows)
https://www.charlesproxy.com/ (Windows, Linux, MacOS, платный, но есть пробная версия)
https://mitmproxy.org/ (Linux, MacOS)
https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project (Windows, LInux, MacOS)
Инициализируйте драйвер так, чтобы запросы из браузера отправлялись через этот прокси-сервер, убедитесь, что они там видны."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.proxy import *


options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём в опции хрома, что он запуститься во весь экран
# options.add_argument("--headless")


# вариант 1 - РАБОЧИЙ
# myProxy = "192.168.100.197:8888"
# options.add_argument(f'--proxy-server={myProxy}')

# вариант 2 - РАБОЧИЙ
# options.proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': '192.168.100.197:8888'})

# вариант 3 - РАБОЧИЙ
# myProxy = "192.168.100.197:8888"
# options.proxy = Proxy({'proxyType': ProxyType.MANUAL,"socksVersion": 5,'httpProxy': myProxy,'sslProxy': myProxy,"socksProxy": myProxy,'noProxy':''})

# вариант 4 - РАБОЧИЙ
myProxy = "192.168.100.197:8888"
options.add_argument('--proxy-server=%s' % myProxy)


driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://192.168.100.197/litecart/admin/login.php')

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


time.sleep(10)
driver.quit()


# driver = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}})