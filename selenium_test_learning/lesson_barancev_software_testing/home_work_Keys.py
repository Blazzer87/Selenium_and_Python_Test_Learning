import time
from selenium import webdriver
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')


driver = webdriver.Chrome(options)
driver.get("https://reestr-hello-linux.qpdev.ru/registration")

input_field = driver.find_element('xpath', '//input[@name="lastName"]')

time.sleep(2)
input_field.send_keys(Keys.CONTROL, 'V')
time.sleep(2)


