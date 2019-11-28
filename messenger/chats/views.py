from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from chats.models import Chat, Message
from users.models import User, Member
from chats.form import MessageForm, ChatForm
from users.form import MemberForm
from django.shortcuts import get_object_or_404

def chat_list(request):
    if request.method == "GET":
        chat_list = Chat.objects.values('id')
        return JsonResponse({'chat list: ' : list(chat_list)})
    return HttpResponseNotAllowed(['GET'])

def one_chat(request, id):
    if request.method == "GET":
        chat = Chat.objects.all()
        chat = chat.get(id=id)
        return JsonResponse({'chat': chat.id, 'topic': chat.topic, 'last message': chat.last_message})
    return HttpResponseNotAllowed(['GET'])

def create_chat(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_id = request.POST.get('user', False)
            if not user_id:
                return HttpResponseBadRequest
            is_group_chat = request.POST.get('is_group_chat', False)
            topic = request.POST.get('topic')
            last_message = request.POST.get('last_message')
            user = User.objects.get(id=user_id)
            new_chat = Chat.objects.create(is_group_chat = is_group_chat, topic = topic)
            new_member = Member.objects.create(user = user, chat = new_chat, new_messages = 0, last_read_message_id = last_message)
            return JsonResponse({'new chat': new_chat.id, 'topic': new_chat.topic})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])

def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            chat_id = request.POST.get('chat', False)
            user_id = request.POST.get('user', False)
            content = request.POST.get('content', False)
            added_at = request.POST.get('added_at', False)
            if not (chat_id or user_id or content):
                return HttpResponseBadRequest
            chat = Chat.objects.get(id = chat_id)
            user = User.objects.get(id = user_id)
            new_mess = Message.objects.create(chat = chat, user = user, content = content, added_at = added_at)
            return JsonResponse({'user: ' : new_mess.user_id, 'new message: ': new_mess.content})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])

def list_messages(request):
    if request.method == "GET":
        messages = Message.objects.values('id', 'content')
        return JsonResponse({'messages: ' : list(messages)})
    return HttpResponseNotAllowed(['GET'])

def read_message(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member_id = request.POST.get('member', False)
            if not member_id:
                return HttpResponseBadRequest
            member = get_object_or_404(Member, id = member_id)
            chat_id = member.chat.id
            messages = Message.objects.all().filter(chat_id = chat_id).order_by('added_at')
            member.last_read_message = messages.last()
            return JsonResponse({'last read message' : member.last_read_message.id})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])