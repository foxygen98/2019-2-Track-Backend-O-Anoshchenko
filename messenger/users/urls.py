from .views import profile, contacts, search_profile
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('<int:prof_id>', profile, name='profile'),
    path('contacts/', contacts, name='contacts'),
    path('profile/search/<str:nick>', search_profile, name='search_profile')
] + router.urls
