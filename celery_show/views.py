from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .task import *
# Create your views here.


# def send_mail_without_celery():
#     send_mail('CELERY WORKED', 'THIS IS MESSAGE BODY',
#               'gopaleswor@gopaleswortours.com.np', ['thapabishnu20@gmail.com'], fail_silently=False)
#     # from mail and to mail
#     return None


def index(request):
    send_mail_task.delay()

    # send_mail_without_celery()

    # task.sleepy(10)
    # task.sleepy.delay(10)
    return HttpResponse('<h1>Hello Form Celery </h1>')
