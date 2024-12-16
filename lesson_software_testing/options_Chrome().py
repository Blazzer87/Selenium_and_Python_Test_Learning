from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')                 # развернуть браузер на весь экран
options.add_argument('incognito')                       # запуск в режиме инкогнито
options.add_argument("--deny-permission-prompts")       # запрет на выдачу запросов на разрешения (например о местоположении)
options.page_load_strategy = 'eager'                    # меняем стратегию загрузки страницы на более раннюю
options.add_argument("--headless")                      # Запуск в фоновом режиме, без открытия браузера


# options.add_argument("--enable-logging")            # Включение логирования - НЕ СРАБОТАЛИ, перепроверять
# options.add_argument("--v=3")                       # Уровень логирования - НЕ СРАБОТАЛИ, перепроверять