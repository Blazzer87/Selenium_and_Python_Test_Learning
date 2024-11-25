import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

user_input = 0
while user_input == 0:

    driver.get('https://reestr-hello-linux.qpdev.ru/')
    time.sleep(4)
    # нажать кнопку регистрации
    registration = driver.find_element(By.CSS_SELECTOR, '[class=qpd-rstr--register-0-2-54]')
    registration.click()
    # нажать кнопку фамилия
    lastname = driver.find_element(By.CSS_SELECTOR, '[name=lastName]')
    lastname.send_keys('Лаба')
    # нажать кнопку имя
    firstname = driver.find_element(By.CSS_SELECTOR, '[name=firstName]')
    firstname.send_keys('Сергей')
    # нажать кнопку отчество
    middlename = driver.find_element(By.CSS_SELECTOR, '[name=middleName]')
    middlename.send_keys('Александрович')
    # ввести телефон
    phone = driver.find_element(By.CSS_SELECTOR, '[name=phone]')
    phone.send_keys('79507586687')
    # ввести инн
    inn = driver.find_element(By.CSS_SELECTOR, '[name=inn]')
    inn.send_keys('871204050495')
    # ввести снилс
    snils = driver.find_element(By.CSS_SELECTOR, '[name=snils]')
    snils.send_keys('12345678912')
    # ввести пароль
    password_reg = driver.find_element(By.CSS_SELECTOR, '[name=password]')
    password_reg.send_keys('!QAZ1qaz')
    # ввести подтверждение пароля
    password_reg_again = driver.find_element(By.CSS_SELECTOR, '[name=passwordAgain]')
    password_reg_again.send_keys('!QAZ1qaz')
    # ввести паспорт
    passport = driver.find_element(By.CSS_SELECTOR, '[name=document]')
    passport.send_keys('4509917635')
    # ввести почту
    passport = driver.find_element(By.CSS_SELECTOR, '[name=email]')
    passport.send_keys('s.laba@qpdev.ru')
    # нажать зарегистрироваться
    # registration_button = driver.find_element(By.CSS_SELECTOR, '[type=submit]')
    # registration_button.click()

    time.sleep(5)

    user_input = int(input("Если пробуем снова то введи 0?"))

driver.quit()
exit()