from rest_framework import serializers
from .models import Chat, Message
from users.models import Member

class ChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Chat
        fields = ['is_group_chat', 'topic', 'last_message']

class MemberSerializer(serializers.ModelSerializer):
    chat_topic = serializers.ReadOnlyField(source='chat.topic')

    class Meta:
        model = Member
        fields = ['chat_id', 'chat_topic']

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['chat', 'user', 'content', 'added_at']