from django.http import JsonResponse
from django.http import HttpResponseNotAllowed

def chat_list(request, id):
    if request.method == "GET":
        chat_list = request.GET.get('chat_list')
        return JsonResponse({'first chat': 'Lena', 'second chat': 'Kolya'})
    else:
        return HttpResponseNotAllowed(['GET'])

def one_chat(request, id):
    if request.method == "GET":
        chat = request.GET.get('chat')
        return JsonResponse({'message': 'Hello!', 'time': '22:22'})
    else:
        return HttpResponseNotAllowed(['GET'])
