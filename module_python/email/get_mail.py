import imaplib
import email
from email.header import decode_header


input_email = 's.laba@qpdev.ru'
password_input_email = 'RatYTrTa9m2_'
password_IDE = 'vLuxBLs7Bh23ekSziqq8'

input_yandex_email = 'laba87-test1@yandex.ru'
password_IDE_yandex = 'dsnkgiqxrulmohyq'


def get_mail():

    mail = imaplib.IMAP4_SSL("imap.mail.ru")        # подключаемся к серверу
    try:
        mail.login(input_email, password_IDE)           # логинимся
        mail.select('inbox')                            # выбираем папку которую будем проверять

        status, messages = mail.search(None, 'UNSEEN')
        mail_ids = messages[0].split()

        # Получаем последние 5 писем
        if mail_ids:
            last_email_id = mail_ids[-1]
            status, msg_data = mail.fetch(last_email_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])

            # Декодируем заголовок "От"
            sender = decode_header(msg['From'])[0][0]
            if isinstance(sender, bytes):
                sender = sender.decode()

            # Декодируем заголовок "Тема"
            subject = decode_header(msg['Subject'])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()

            # Декодируем тело сообщения
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        # Если часть - текстовая
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break  # Выходим из цикла после первого текстового содержимого
                else:
                    # Если сообщение не многочастное
                    body = msg.get_payload(decode=True).decode()

                print(f'От: {sender}, Тема: {subject}')
                print(body)

                return sender, subject

    except Exception as e:
        print("Ошибка:", e)

    finally:
        mail.logout()



get_mail()




"""
    НАСТРОЙКИ mail.search
    1. ALL: Все сообщения.
    2. ANSWERED: Сообщения с ответом.
    3. UNANSWERED: Сообщения без ответа.
    4. DELETED: Удаленные сообщения.
    5. FLAGGED: Сообщения с флагом "важное".
    6. UNFLAGGED: Сообщения без флага "важное".
    7. NEW: Новые сообщения (не прочитанные).
    8. OLD: Старые сообщения (прочитанные).
    9. SEEN: Прочитанные сообщения.
    10. UNSEEN: Непрочитанные сообщения.
    11. FROM "имя": Сообщения от указанного отправителя.
    12. TO "имя": Сообщения, адресованные указанному получателю.
    13. SUBJECT "тема": Сообщения с указанной темой.
    14. BODY "текст": Сообщения с указанным текстом в теле.
    15. CC "имя": Сообщения с указанным адресом в копии.
    16. BCC "имя": Сообщения с указанным адресом в скрытой копии.
    17. SINCE "дата": Сообщения, полученные с указанной даты (формат: "01-Jan-2023").
    18. BEFORE "дата": Сообщения, полученные до указанной даты.
    19. ON "дата": Сообщения, полученные в указанный день.
    20. LARGER N: Сообщения, размер которых больше N байт.
    21. SMALLER N: Сообщения, размер которых меньше N байт.
    """