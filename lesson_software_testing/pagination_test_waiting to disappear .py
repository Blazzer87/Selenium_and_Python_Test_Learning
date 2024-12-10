import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('https://pagination.js.org/')
driver.implicitly_wait(2)

number1 = driver.find_element(By.XPATH, '//*[@id="demo1"]/div[1]/ul/li[1]')         # запрашиваем  элемент и его текст
print('Текст первоначального элемента', number1.text)                                                                         # текст элемента 1

page2 = driver.find_element(By.XPATH, '//*[@id="demo1"]/div[2]/div/ul/li[3]/a')     # находим кнопку пагинации
page2.click()                                                                               # нажимаем пагинацию, перелистываем записи

wait = WebDriverWait(driver, 2) # seconds       # требует импорта библиотек, создаём 2-ух секундное ожидание
wait.until(EC.staleness_of(number1))                    # ожидает исчезновения, убеждаемся что элемент исчез

number1 = driver.find_element(By.XPATH, '//*[@id="demo1"]/div[1]/ul/li[1]')         # запрашиваем заново элемент и его текст - видим новый получившийся элемент
print('Текст нового элемента', number1.text)                                                                        #  текст нового элемента 11

driver.close()


wait = WebDriverWait(driver, 2) # seconds
wait.until(EC.visibility_of(number1))                                                       # обратный алгоритм ожидания видимости элемента