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
        users = User.objects.filter(nick__icontains = nick) | \
            User.objects.filter(first_name__icontains = nick) | \
            User.objects.filter(last_name__icontains = nick)
        users = users.values('nick', 'first_name', 'last_name')
        return JsonResponse({'users ': list(users)})
    return HttpResponseNotAllowed(['GET'])