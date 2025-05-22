import time
from module_python.email.get_mail import get_mail
from module_python.email.reply_email import reply_email

if __name__ == "__main__":
    while True:
        unread_emails = get_mail()
        if unread_emails:
            for email_info in unread_emails:
                reply_email(unread_emails[0],unread_emails[1])
                print("сообщение отправлено")
        time.sleep(10)

