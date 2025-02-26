# установим и настроим ChromeDriver с помощью команд в терминале. Укажем нужную нам версию ChromeDriver для загрузки.
# Для получения ссылки перейдите в браузере на нужную вам версию драйвера по ссылке на https://sites.google.com/chromium.org/driver/.
# На открывшейся странице нажмите на файле для Linux правой кнопкой и скопируйте путь к файлу.
# Замените в примере ниже путь к файлу для команды wget вашей ссылкой:
# wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip
# Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
# sudo mv chromedriver /usr/local/bin/chromedriver
# sudo chown root:root /usr/local/bin/chromedriver
# sudo chmod +x /usr/local/bin/chromedriver
# Проверьте, что chromedriver доступен, выполнив команду chromedriver в терминале, вы должны получить сообщение о том, что процесс успешно запущен

# гекодрайвер для Firefox устанавливается и запускается аналогично - проверено.

# скачать селениум сервер на удалённую машину,
# на убунту поместить jar файл селениум сервера в HOME
# запустить через команду


from selenium import webdriver
import time

options = webdriver.FirefoxOptions()
driver1 = webdriver.Remote(command_executor="http://192.168.182.137:4444/wd/hub", options=options)

driver1.get('https://www.google.com/')


options = webdriver.ChromeOptions()
driver2 = webdriver.Remote(command_executor="http://192.168.182.137:4444/wd/hub", options=options)

driver2.get('https://www.avito.ru/')

time.sleep(30)
driver1.quit()
driver2.quit()


























