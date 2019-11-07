from django.http import JsonResponse

# Create your views here.
def chat_list(request, id):
    if request.method == "GET":
        try:
            chat_list = request.GET.get('chat_list')
        except ChatList.DoesNotExist:
            raise Http404
        return JsonResponse({'first chat': 'Lena', 'second chat': 'Kolya'})
    else:
        raise Http405

def one_chat(request, id):
    if request.method == "GET":
        try:
            chat = request.GET.get('chat')
        except Chat.DoesNotExist:
            raise Http404
        return JsonResponse({'message': 'Hello!', 'time': '22:22'})
    else:
        raise Http405