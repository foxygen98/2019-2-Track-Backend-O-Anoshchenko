from django.db import models

class Chat(models.Model):
    is_group_chat = models.BooleanField(default=False, verbose_name='Групповой чат')
    topic = models.TextField(verbose_name='Тема')
    last_message = models.TextField(verbose_name='Последнее сообщение')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, verbose_name="id чата")
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="id пользователя")
    content = models.TextField(verbose_name='Текст сообщения')
    added_at = models.DateTimeField(verbose_name="Время отправки", null=False, auto_now=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('-added_at',)

class Attachment(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, verbose_name="id чата")
    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name="id пользователя")
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="id сообщения")
    type_of_attach = models.CharField(max_length=16, default='', verbose_name="Тип вложения")
    url = models.URLField(verbose_name="Ссылка на вложение")

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
