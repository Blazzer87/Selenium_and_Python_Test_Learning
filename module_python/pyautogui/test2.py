import pyautogui
import time

# Подождите немного, чтобы вы могли переключиться на текстовый редактор
time.sleep(5)
pyautogui.FAILSAFE = True


# Ввод текста
pyautogui.write('Hello, this is an automated message!', interval=0.1)
pyautogui.write('Hello, this is an automated message!', interval=0.1)
pyautogui.write('Hello, this is an automated message!', interval=0.1)
pyautogui.write('Hello, this is an automated message!', interval=0.1)
pyautogui.write('Hello, this is an automated message!', interval=0.1)
pyautogui.press('enter')
pyautogui.write('This was typed using PyAutoGUI.')
