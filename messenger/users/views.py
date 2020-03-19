from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from users.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q

def profile(request, prof_id):
    if request.method == "GET":
        profile = User.objects.values('id', 'username', 'nick')
        profile = get_object_or_404(profile, id=prof_id)
        return JsonResponse({'profile': profile})
    return HttpResponseNotAllowed(['GET'])

def contacts(request, prof_id):
    if request.method == "GET":
        return JsonResponse({'contacts': 'test'})
    return HttpResponseNotAllowed(['GET'])

def search_profile(request, nick):
    if request.method == "GET":
        users = User.objects.filter(
            Q(nick__icontains=nick)|
            Q(last_name__icontains=nick)|
            Q(first_name__icontains=nick)
        ).values('nick')
        return JsonResponse({'users': list(users)})
    return HttpResponseNotAllowed(['GET'])