from chats.views import chat_list, one_chat, create_chat
from chats.views import send_message, list_messages, read_message
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('chat_list/', chat_list, name='chat_list'),
    path('one_chat/<int:id>/', one_chat, name='one_chat'),
    path('create_chat/', csrf_exempt(create_chat), name='create_chat'),
    path('send_message/', csrf_exempt(send_message), name='send_message'),
    path('list_messages/', list_messages, name='list_messages'),
    path('read_message/', csrf_exempt(read_message), name='read_message'),
]
