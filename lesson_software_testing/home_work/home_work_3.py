import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://localhost/litecart/admin/login.php')
time.sleep(1)               # для отслеживания действий
username = driver.find_element(By.CSS_SELECTOR, '[name=username]')
username.send_keys('admin')
time.sleep(1)               # для отслеживания действий
password = driver.find_element(By.CSS_SELECTOR, '[name=password]')
password.send_keys('admin')
time.sleep(1)               # для отслеживания действий
rememberme = driver.find_element(By.CSS_SELECTOR, '[name=remember_me]')
rememberme.click()
time.sleep(1)               # для отслеживания действий
submit = driver.find_element(By.CSS_SELECTOR, '[name=login]')
submit.click()
time.sleep(3)              # для отслеживания действий
driver.quit()