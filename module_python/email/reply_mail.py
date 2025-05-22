from module_python.email.send_mail import send_mail
from module_python.email.get_mail import get_mail


def reply_email(x, y):
        reply_subject = f"Re: {y}"
        send_mail(recipient=x,
                        subject=reply_subject,
                        message_body="Привет, спасибо за информацию!")


