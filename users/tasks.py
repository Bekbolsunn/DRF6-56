from celery import shared_task
import time
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_otp_email(email, code):
    print("Starting...")
    time.sleep(10)
    send_mail(
        "Привет новый пользователь!",
        f"Ваш одноразовый код: {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
    print("Done")
    return "Ok"

@shared_task
def send_daily_report():
    print("Report...")
    email = "karataevbekbolsun@gmail.com"
    send_mail(
        "Здравствуйте, босс!",
        f"Вот ваш отчет за неделю: 🐸",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
    print("Send")
    return "Ok"
