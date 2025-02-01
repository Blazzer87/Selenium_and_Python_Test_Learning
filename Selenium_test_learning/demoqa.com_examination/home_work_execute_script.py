import time

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options)

driver.get('https://demoqa.com/login')

element = driver.find_element('xpath', '//div[@class="element-list collapse"]')

time.sleep(3)
js_code = "var collapseElement = document.querySelector('.element-list.collapse'); if (collapseElement) {collapseElement.style.display = 'block';}"

driver.execute_script(js_code)
time.sleep(3)
