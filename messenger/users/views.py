from django.http import JsonResponse

# Create your views here.
def profile(request, id):
    if request.method == "GET":
        try:
            profile = request.GET.get('profile')
        except Profile.DoesNotExist:
            raise Http404
        return JsonResponse({'Name':'Oksana', 'Age':'21'})
    else:
        raise Http405

def contacts(request, id):
    if request.method == "GET":
        try:
            contacts = request.GET.get('contacts')
        except Contacts.DoesNotExist:
            raise Http404
        return JsonResponse({'name': 'Katya', 'phone number': '8 912 345 67 89'})
    else:
        raise Http405