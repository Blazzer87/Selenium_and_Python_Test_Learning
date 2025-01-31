import time
from selenium import webdriver
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options)
driver.get("https://demoqa.com/menu")

MI1 = driver.find_element('xpath', '//a[text()="Main Item 1"]')
MI2 = driver.find_element('xpath', '//a[text()="Main Item 2"]')
MI3 = driver.find_element('xpath', '//a[text()="Main Item 3"]')
SUBSUBLIST = driver.find_element('xpath', '//a[text()="SUB SUB LIST »"]')
SubSubItem2 = driver.find_element('xpath', '//a[text()="Sub Sub Item 2"]')


action = ActionChains(driver)
action.move_to_element(MI1)
action.pause(1)
action.move_to_element(MI3)
action.pause(1)
action.move_to_element(MI2)
action.pause(1)
action.move_to_element(SUBSUBLIST)
action.pause(1)
action.move_to_element(SubSubItem2)
action.click(SubSubItem2)
action.perform()

time.sleep(3)