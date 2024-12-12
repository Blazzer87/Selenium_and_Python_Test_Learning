import time
import random

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('incognito')
driver = webdriver.Chrome(options)

driver.get('https://t-hello.aoreestr.ru/')


WebDriverWait(driver, 30).until(expected_conditions.alert_is_present())

alert = Alert(driver)

alert.accept()          #  "Разрешить всегда"
# alert.dismiss()         #  "Не разрешать"


time.sleep(10)