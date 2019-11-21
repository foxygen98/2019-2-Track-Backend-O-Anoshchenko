from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from chats.models import Chat
from users.models import User, Member

def chat_list(request, id):
    if request.method == "GET":
        chat_list = Chat.objects.all()
        chat_list = chat_list.filter(user__id = id)
        return JsonResponse({'first chat': 'Lena', 'second chat': 'Kolya'})
    return HttpResponseNotAllowed(['GET'])

def one_chat(request, id):
    if request.method == "GET":
        chat = request.GET.get('chat')
        return JsonResponse({'message': 'Hello!', 'time': '22:22'})
    return HttpResponseNotAllowed(['GET'])

def create_chat(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id', False)
        if not user_id:
            return HttpResponseBadRequest
        is_group_chat = request.POST.get('is_group_chat', False)
        topic = request.POST.get('topic')
        user = User.objects.get(id=user_id)
        new_chat = Chat.objects.create(is_group_chat = is_group_chat, topic = topic)
        new_member = Member.objects.create(user = user, chat = new_chat, new_messages = 0)
        return JsonResponse({'OK': '!'})
    return HttpResponseNotAllowed(['POST'])