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
    time.sleep(2)
    registration = driver.find_element(By.CSS_SELECTOR, '[class=qpd-rstr--register-0-2-54]')
    registration.click()
    lastname = driver.find_element(By.CSS_SELECTOR, '[name=lastName]')
    lastname.send_keys('Фролов')
    firstname = driver.find_element(By.CSS_SELECTOR, '[name=firstName]')
    firstname.send_keys('Миша')

    time.sleep(10)

    user_input = int(input("Если пробуем снова то введи 0?"))

driver.quit()
exit()