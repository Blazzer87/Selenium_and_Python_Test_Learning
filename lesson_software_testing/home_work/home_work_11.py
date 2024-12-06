'''
Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart
(не в админке, а в клиентской части магазина).
Сценарий должен состоять из следующих частей:
1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты
(чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария),
2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
3) повторный вход в только что созданную учётную запись,
4) и ещё раз выход.
В качестве страны выбирайте United States, штат произвольный. При этом формат индекса -- пять цифр.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(2)

reg_data = [
    {'tax_id':'12345'},
    {'company': 'QPD'},
    {'firstname':'Sergey'},
    {'lastname':'Laba'},
    {'address1':'Pobedi 60'},
    {'address2':'kv. 90'},
    {'postcode':'55555'}
    ]

registration_button = driver.find_element(By.XPATH, '//*[@id="box-account-login"]//a[text()="New customers click here"]')
registration_button.click()

tax_id = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="tax_id"]')
tax_id.send_keys('12345')

company = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="company"]')
company.send_keys('QPD')

first_name = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="firstname"]')
first_name.send_keys('Sergey')

last_name = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="lastname"]')
last_name.send_keys('Laba')

address1 = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="address1"]')
address1.send_keys('Pobedi 60')

address2 = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="address2"]')
address2.send_keys('kv. 90')

postcode = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="postcode"]')
postcode.send_keys('55555')

city = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="city"]')
city.send_keys('Voronezh')

email = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="email"]')
email.send_keys('laba@laba.ru')

password = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="password"]')
password.send_keys('!QAZ1qaz')

confirmed_password = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="confirmed_password"]')
confirmed_password.send_keys('!QAZ1qaz')

phone = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="phone"]')
phone.send_keys('79507586687')







time.sleep(5)
driver.quit()

