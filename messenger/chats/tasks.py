from application.celery import app
from django.core.mail import send_mail
from application.settings import EMAIL_HOST_USER
from .models import Chat

@app.task()
def add_together(a, b):
    return a + b

@app.task(time_limit=60)
def send_email(email):
    send_mail(
        'New chat!', #передавать информацию о созданном чате
        'Hello! It`s a new chat! :)',
        EMAIL_HOST_USER,
        email,
        fail_silently=False,
    )

def num_of_chats():
    return len(Chat.objects.all())

@app.task()
def send_report():
    send_mail(
        'Report',
        'Hello! Today we have ' + str(num_of_chats()) + ' chats!', #изменить на более быстрый способ
        EMAIL_HOST_USER,
        ['anoschenko.ov@phystech.edu'],
        fail_silently=False,
    )
