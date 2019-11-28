from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from users.models import User

def profile(request, id):
    if request.method == "GET":
        profile = User.objects.all()
        profile = profile.get(id = id)
        return JsonResponse({'id': profile.id, 'nick': profile.nick})
    return HttpResponseNotAllowed(['GET'])

def contacts(request, id):
    if request.method == "GET":
        contacts = request.GET.get('contacts')
        return JsonResponse({'name': 'Katya'})
    return HttpResponseNotAllowed(['GET'])

def search_profile(request, nick):
    if request.method == "GET":
        user = User.objects.all()
        user = user.get(nick = nick)
        return JsonResponse({'user': user.id, 'nick': user.nick})
    return HttpResponseNotAllowed(['GET'])