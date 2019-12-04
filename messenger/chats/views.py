from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from chats.models import Chat, Message
from users.models import User, Member
from chats.form import MessageForm, ChatForm
from django.shortcuts import get_object_or_404

def chat_list(request, id):
    if request.method == "GET":
        members = Member.objects.filter(user = id)
        members = members.values('chat')
        return JsonResponse({'chat list: ' : list(members)})
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
        user_id = request.POST.get('user')
        if form.is_valid():
            chat = form.save()
            #user = get_object_or_404(User, id = user_id)
            user = User.objects.get(id=user_id)
            member = Member.objects.create(user=user, chat=chat, last_read_message_id=0)
            return JsonResponse({'new chat': chat.id, 'topic': chat.topic, 'member': member.id})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])

def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            return JsonResponse({'user: ' : message.user_id, 'new message: ': message.content})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])

def list_messages(request, chat_id):
    if request.method == "GET":
        messages = Message.objects.filter(chat=chat_id)
        messages = messages.values('id', 'content')
        return JsonResponse({'messages: ' : list(messages)})
    return HttpResponseNotAllowed(['GET'])

def read_message(request):
    if request.method == "POST":
        member_id = request.POST.get('member')
        member = get_object_or_404(Member, id = member_id)
        chat_id = member.chat.id
        messages = Message.objects.all().filter(chat_id = chat_id).order_by('added_at')
        member.last_read_message_id = messages.last().id
        return JsonResponse({'last read message' : member.last_read_message_id})
    return HttpResponseNotAllowed(['POST'])