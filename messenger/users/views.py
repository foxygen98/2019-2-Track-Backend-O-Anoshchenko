from django.http import JsonResponse
from django.http import HttpResponseNotAllowed

def profile(request, id):
    if request.method == "GET":
        profile = request.GET.get('profile')
        return JsonResponse({'Name':'Oksana', 'Age':'21'})
    else:
        return HttpResponseNotAllowed(['GET'])

def contacts(request, id):
    if request.method == "GET":
        contacts = request.GET.get('contacts')
        return JsonResponse({'name': 'Katya', 'phone number': '8 912 345 67 89'})
    else:
        return HttpResponseNotAllowed(['GET'])
