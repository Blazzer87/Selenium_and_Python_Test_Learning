'''
Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart (не в админке, а в клиентской части магазина).
Сценарий должен состоять из следующих частей:
1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты (чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария),
2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
3) повторный вход в только что созданную учётную запись,
4) и ещё раз выход.
В качестве страны выбирайте United States, штат произвольный. При этом формат индекса -- пять цифр.
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

registration_button = driver.find_element(By.XPATH, '//*[@id="box-account-login"]//a[text()="New customers click here"]')
registration_button.click()



time.sleep(5)
driver.quit()

