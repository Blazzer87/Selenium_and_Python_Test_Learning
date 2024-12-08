'''
Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart
(не в админке, а в клиентской части магазина).
Сценарий должен состоять из следующих частей:
1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты
(чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария),
2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
3) повторный вход в только что созданную учётную запись,
4) и ещё раз выход.
В качестве страны выбирайте United States, штат произвольный. При этом формат индекса -- пять цифр.
'''

import faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
options.add_argument('incognito')                   # передаём инкогнито в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(2)

fake_email = faker.Faker().email()
print("Используемая почта:", fake_email)

reg_data = {
    'tax_id':'454545',
    'company': 'QPD',
    'firstname':'Sergey',
    'lastname':'Laba',
    'address1':'Pobedi 60',
    'address2':'kv. 90',
    'postcode':'55555',
    'city':'Voronezh',
    'country':'United States',
    'email':f'{fake_email}',
    'phone':'79507586687',
    'password':'!QAZ1qaz',
    'confirmed_password':'!QAZ1qaz'
    }

registration_button = driver.find_element(By.XPATH, '//*[@id="box-account-login"]//a[text()="New customers click here"]')
registration_button.click()

tax_id = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="tax_id"]')
tax_id.send_keys(f'{reg_data.get('tax_id')}')

company = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="company"]')
company.send_keys(f'{reg_data.get('company')}')

firstname = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="firstname"]')
firstname.send_keys(f'{reg_data.get('firstname')}')

lastname = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="lastname"]')
lastname.send_keys(f'{reg_data.get('lastname')}')

address1 = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="address1"]')
address1.send_keys(f'{reg_data.get('address1')}')

address2 = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="address2"]')
address2.send_keys(f'{reg_data.get('address2')}')

postcode = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="postcode"]')
postcode.send_keys(f'{reg_data.get('postcode')}')

city = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="city"]')
city.send_keys(f'{reg_data.get('city')}')

email = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="email"]')
email.send_keys(f'{reg_data.get('email')}')

phone = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="phone"]')
phone.send_keys(f'{reg_data.get('phone')}')

password = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="password"]')
password.send_keys(f'{reg_data.get('password')}')

confirmed_password = driver.find_element(By.XPATH, '//*[@id="create-account"]//input[@name="confirmed_password"]')
confirmed_password.send_keys(f'{reg_data.get('confirmed_password')}')

country_selector = driver.find_element(By.CSS_SELECTOR, '[role=presentation]')
country_selector.click()

country_list = driver.find_element(By.CSS_SELECTOR, '[type=search]')
country_list.send_keys(f'{reg_data.get('country')}')
country_list.send_keys(Keys.ENTER)

zone_code = driver.find_element(By.XPATH, '//*[@id="create-account"]//select[@name="zone_code"]')
zone_code.click()
zone = driver.find_element(By.XPATH, '//*[@id="create-account"]//select/option[text()="Nevada"]')
zone.click()
zone_code.click()

create_account = driver.find_element(By.XPATH, '//*[@id="create-account"]//button[@type="submit"]')
create_account.click()

logout_button = driver.find_element(By.XPATH, '//*[@id="box-account"]//a[text()="Logout"]')
logout_button.click()

login_email = driver.find_element(By.XPATH, '//*[@id="box-account-login"]//input[@name="email"]')
login_email.send_keys(fake_email)

login_password = driver.find_element(By.XPATH, '//*[@id="box-account-login"]//input[@name="password"]')
login_password.send_keys(reg_data.get('password'))

login_button = driver.find_element(By.XPATH, '//*[@id="box-account-login"]//button[text()="Login"]')
login_button.click()

logout_button = driver.find_element(By.XPATH, '//*[@id="box-account"]//a[text()="Logout"]')
logout_button.click()

driver.quit()

