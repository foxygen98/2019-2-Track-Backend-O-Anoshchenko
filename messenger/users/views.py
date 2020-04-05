from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from .models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

@login_required
def profile(request, prof_id):
    if request.method == "GET":
        profile = User.objects.values('id', 'username', 'nick')
        profile = get_object_or_404(profile, id=prof_id)
        return JsonResponse({'profile': profile})
    return HttpResponseNotAllowed(['GET'])

@cache_page(60)
@login_required
def contacts(request):
    if request.method == "GET":
        return JsonResponse({'contacts': 'test'})
    return HttpResponseNotAllowed(['GET'])

@login_required
def search_profile(request, nick):
    if request.method == "GET":
        users = User.objects.filter(
            Q(nick__icontains=nick)|
            Q(last_name__icontains=nick)|
            Q(first_name__icontains=nick)
        ).values('nick')
        return JsonResponse({'users': list(users)})
    return HttpResponseNotAllowed(['GET'])

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['GET'])
    def profile(self, request, pk):
        users = self.get_queryset()
        profile = get_object_or_404(users, id=pk)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(profile, many=False)
        return  Response({'profile': serializer.data})

    @cache_page(60)
    @action(detail=False, methods=['GET'])
    def contacts(self, request):
        users = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(users, many=True)
        return Response({'contacts': serializer.data})

    @action(detail=True, methods=['GET'])
    def search_profile(self, request, pk):
        users = self.get_queryset()
        profiles = User.objects.filter(
            Q(nick__icontains=pk)|
            Q(last_name__icontains=pk)|
            Q(first_name__icontains=pk)
        )
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(profiles, many=True)
        return Response({'profiles': serializer.data})
