from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth
from django.http import HttpResponseRedirect
from .forms import AuthForm
from django.views.decorators.csrf import csrf_exempt

def login(request):
    return render(request, 'login.html')

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
    if form.is_valid() and request.recaptcha_is_valid:
        user = authenticate(username=request.POST['username'], 
                            password=request.POST['password'])
        if user is not None:
            auth(request, user)
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render(request, 'home.html')