from chats.views import chat_list, one_chat, create_chat
from chats.views import send_message, list_messages, read_message
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'chats', ChatViewSet, basename='chat')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('chat_list/<int:user_id>/', chat_list, name='chat_list'),
    path('one_chat/<int:chat_id>/', one_chat, name='one_chat'),
    path('create_chat/', create_chat, name='create_chat'),
    path('send_message/', send_message, name='send_message'),
    path('messages/<int:chat_id>/', list_messages, name='list_messages'),
    path('read_message/', read_message, name='read_message'),
] + router.urls
