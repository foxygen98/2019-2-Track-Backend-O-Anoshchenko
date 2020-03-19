import factory
from chats.models import Message

class MessageFactory(factory.Factory):
    class Meta:
        model = Message

    content = 'TestContent'
