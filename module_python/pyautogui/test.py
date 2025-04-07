import pyautogui

pyautogui.moveTo(600, 300, duration=1)  # Переместить курсор в координаты (100, 100) за 1 секунду

pyautogui.click()  # Клик левой кнопкой мыши
pyautogui.click(x=900, y=300)  # Клик в указанных координатах

pyautogui.write('Hello, world!', interval=0.1)  # Печатает текст с задержкой 0.1 секунды между символами

pyautogui.doubleClick()     #    • Двойной клик
pyautogui.rightClick()      #    • Правый клик

pyautogui.press('enter')         # Нажимает клавишу Enter
pyautogui.hotkey('ctrl', 'shift', 'f10')  # Нажимает сочетание клавиш Ctrl+C

screenshot = pyautogui.screenshot()  # Делает скриншот всего экрана
screenshot.save('screenshot.png')  # Сохраняет скриншот в файл

x, y = pyautogui.position()
print(f'Current mouse position: ({x}, {y})')            #  • Получение текущих координат курсора:

pyautogui.FAILSAFE = True       # Включить режим безопасности - прервать выполнение скрипта, если курсор перемещается в один из углов экрана.