from users.views import profile
from users.views import contacts
from django.urls import path

urlpatterns = [
    path('profile/<int:id>/', profile, name='profile'),
    path('contacts/<int:id>/', contacts, name='contacts'),
]
