import time
from selenium import webdriver
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')


driver = webdriver.Chrome(options)
driver.get("http://the-internet.herokuapp.com/dropdown")

