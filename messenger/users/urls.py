from users.views import profile
from users.views import contacts
from users.views import search_profile
from django.urls import path

urlpatterns = [
    path('profile/<int:id>/', profile, name='profile'),
    path('contacts/<int:id>/', contacts, name='contacts'),
    path('profile/search/<str:nick>', search_profile, name='search_profile')
]
