from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    send_mail('CELERY WORKED', "THIS IS MESSAGE BODY",
              'gopaleswor@gopaleswortours.com.np', ["thapabishnu20@gmail.com"], fail_silently=False)
    # from mail and to mail
    return None
