import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://reestr-hello-linux.qpdev.ru/')
phone = driver.find_element(By.NAME, 'phone')
phone.send_keys('79507586687')
password = driver.find_element(By.NAME, 'password')
password.send_keys('!QAZ1qaz')
# submit = driver.find_element(By., 'submit')   код не работает - нужно найти локатор для кнопки
# submit.click()



time.sleep(10)