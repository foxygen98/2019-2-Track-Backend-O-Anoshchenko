from chats.views import chat_list, one_chat, create_chat
from django.urls import path

urlpatterns = [
    path('chat_list/<int:id>/', chat_list, name='chat_list'),
    path('one_chat/<int:id>/', one_chat, name='one_chat'),
    path('create_chat/', create_chat, name='create_chat'),
]
