import time
from selenium import webdriver
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options)
driver.get("https://demoqa.com/droppable")

simple_drag_me = driver.find_element('xpath', '//div[@id="draggable"]')
destination = driver.find_element('xpath', '//div[@id="droppable"]')

action = ActionChains(driver)
action.move_to_element(simple_drag_me)
time.sleep(1)
action.move_to_element(destination)
time.sleep(1)
action.drag_and_drop(simple_drag_me, destination)
action.perform()

assert destination.get_attribute('textContent') == 'Dropped!', 'Что-то пошло не так'

time.sleep(3)