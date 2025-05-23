import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pytest

# данные почтового ящика для исходящей почты
input_email = 's.laba@qpdev.ru'
password_input_email = 'RatYTrTa9m2_'
password_IDE = 'vLuxBLs7Bh23ekSziqq8'

input_yandex_email = 'laba87-test1@yandex.ru'
password_IDE_yandex = 'dsnkgiqxrulmohyq'



def send_mail(recipient, subject, message_body):

    message = MIMEMultipart()           # создали объект сообщения
    message['From'] = input_yandex_email       # добавили в объект сообщения отправителя
    message['To'] = recipient           # добавили в объект сообщения получателя
    message['Subject'] = subject        # добавили в объект сообщения получателя

    message.attach(MIMEText(message_body, 'plain'))     # в объект сообщения мы передаём сообщение,
    # обозначив что его формат будет plain, и это сообщение будет экземпляром класса MIMEText

    try:
        connect = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        # connect.starttls()        используется только с smtplib.SMTP, для незащищенного соединения, которое затем переводится в защищенное.
        connect.login(user = input_yandex_email, password = password_IDE_yandex)
        connect.send_message(msg = message)
        connect.quit()
        print("Сообщение успешно отправлено")
    except Exception as e:
        print("Ошибка отправки сообщения", e)

