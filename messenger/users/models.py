from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nick = models.CharField(max_length=16, verbose_name='Ник')
    avatar = models.ImageField(verbose_name='Аватарка')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Member(models.Model):
    user = models.ForeignKey(
        'User', 
        on_delete=models.CASCADE, 
        verbose_name="id пользователя")
    chat = models.ForeignKey(
        'chats.Chat', 
        on_delete=models.CASCADE, 
        verbose_name="id чата")
    new_messages = models.TextField(verbose_name='Новое сообщение')
    last_read_message = models.ForeignKey(
        'chats.Message', 
        on_delete=models.PROTECT, 
        verbose_name="Последнее прочтенное сообщение"
        )

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

