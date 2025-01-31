import time

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
# options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options)

driver.get('https://www.ozon.ru/')

# element = driver.find_element('xpath', '//div[@class="vue-portal-target"]') - так называется элемент

time.sleep(3)
js_code = "var ELEMENT = document.querySelector('.vue-portal-target'); if (ELEMENT) {ELEMENT.style.display = 'block';}"

driver.execute_script(js_code)
time.sleep(3)

js_code = "var ELEMENT = document.querySelector('.vue-portal-target'); if (ELEMENT) {ELEMENT.style.display = 'none';}"

driver.execute_script(js_code)
time.sleep(3)

js_code = "var ELEMENT = document.querySelector('tm-entity-image__pic'); if (ELEMENT) {ELEMENT.style.display = 'block';}"

driver.execute_script(js_code)
time.sleep(3)

