from core.views import UserCreateView
from django.urls import path

urlpatterns = [
    path('sign-up/', UserCreateView.as_view(), name='register'),
    
]