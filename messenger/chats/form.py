from django import forms
from chats.models import Chat, Message

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['is_group_chat', 'topic', 'last_message']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['chat', 'user', 'content', 'added_at']