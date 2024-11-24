import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

test_data = {'lastName': 'Лаба',
             'firstName': 'Сергей',
             'middleName': 'Александрович',
             'phone': '79507586687',
             'inn': '871204050495',
             'snils': '12345678912',
             'password': '!QAZ1qaz',
             'passwordAgain': 'QAZ1qaz',
             'document': '4509917635',
             'email': 's.laba@qpdev.ru'}

driver.get('https://hello.aoreestr.ru/')
time.sleep(8)
# нажать кнопку регистрации
registration = driver.find_element(By.CSS_SELECTOR, '[class=qpd-rstr--register-0-2-54]')
registration.click()
# нажать кнопку фамилия
lastName = driver.find_element(By.CSS_SELECTOR, '[name=lastName]')
lastName.send_keys(test_data['lastName'])
# нажать кнопку имя
firstName = driver.find_element(By.CSS_SELECTOR, '[name=firstName]')
firstName.send_keys(test_data['firstName'])
# нажать кнопку отчество
middleName = driver.find_element(By.CSS_SELECTOR, '[name=middleName]')
middleName.send_keys(test_data['middleName'])
# ввести телефон
phone = driver.find_element(By.CSS_SELECTOR, '[name=phone]')
phone.send_keys(test_data['phone'])
# ввести инн
inn = driver.find_element(By.CSS_SELECTOR, '[name=inn]')
inn.send_keys(test_data['inn'])
# ввести снилс
snils = driver.find_element(By.CSS_SELECTOR, '[name=snils]')
snils.send_keys(test_data['snils'])
# ввести пароль
password_reg = driver.find_element(By.CSS_SELECTOR, '[name=password]')
password_reg.send_keys(test_data['password'])
# ввести подтверждение пароля
password_reg_again = driver.find_element(By.CSS_SELECTOR, '[name=passwordAgain]')
password_reg_again.send_keys(test_data['passwordAgain'])
# ввести паспорт
passport = driver.find_element(By.CSS_SELECTOR, '[name=document]')
passport.send_keys(test_data['document'])
# ввести почту
passport = driver.find_element(By.CSS_SELECTOR, '[name=email]')
passport.send_keys(test_data['email'])
# нажать зарегистрироваться
registration_button = driver.find_element(By.CSS_SELECTOR, '[type=submit]')
registration_button.click()
# вводим код подтверждения на странице СМС подтверждения
sms = driver.find_element(By.CSS_SELECTOR, '[name=code]')
sms.send_keys('000000')
time.sleep(5)