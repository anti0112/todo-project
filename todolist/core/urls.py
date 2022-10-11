from core.views import UserCreateView
from django.urls import path

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='register'),
    
]