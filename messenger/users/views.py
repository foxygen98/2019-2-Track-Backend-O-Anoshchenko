from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from users.models import User

def profile(request, id):
    if request.method == "GET":
        profile = request.GET.get('profile')
        return JsonResponse({'Name':'Oksana', 'Age':'21'})
    return HttpResponseNotAllowed(['GET'])

def contacts(request, id):
    if request.method == "GET":
        contacts = request.GET.get('contacts')
        return JsonResponse({'name': 'Katya', 'phone number': '8 912 345 67 89'})
    return HttpResponseNotAllowed(['GET'])

def search_profile(request, nick):
    if request.method == "GET":
        user = User.objects.all()
        user = user.filter(nick__contains = nick)
        return JsonResponse({'nick': 'oxy'})
    return HttpResponseNotAllowed(['GET'])