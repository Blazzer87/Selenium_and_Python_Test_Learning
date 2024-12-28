from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# возвращает первый из найденных елс ина странице несколько
form1 = driver.find_element(By.ID, "login-form")
form2 = driver.find_element(By.TAG_NAME, "form")
form3 = driver.find_element(By.CLASS_NAME, "login")
form4 = driver.find_element(By.CSS_SELECTOR, "form.login")
form5 = driver.find_element(By.CSS_SELECTOR, "#login-form")

field1 = driver.find_element(By.NAME, "username")
field2 = driver.find_element(By.XPATH, "//input[@name='username']")
linke1 = driver.find_element(By.LINK_TEXT, "Logout")
linke2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")

linkes = driver.find_elements(By.TAG_NAME, "a")     # возвращает в виде списка найденные на странице в порядке как расположены в ДОМе



# form1 = driver.# find_element - это метод #(By.ID - как искать, "login-form" - что искать) - это параметр





