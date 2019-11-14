from django.db import models

class Chat(models.Model):
    is_group_chat = models.BooleanField(default=False)
    topic = models.TextField()
    last_message = models.TextField()

class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    added_at = models.DateTimeField()

class Attachment(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=16)
    url = models.URLField()
