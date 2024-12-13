from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')                 # развернуть браузер на весь экран
options.add_argument('incognito')                       # запуск в режиме инкогнито
options.add_argument("--deny-permission-prompts")       # запрет на выдачу запросов на разрешения
options.page_load_strategy = 'eager'                    # меняем стратегию загрузки страницы на более раннюю
