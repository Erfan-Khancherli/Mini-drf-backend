
from django.urls import path, include
from .api import RegisterApi ,User

urlpatterns = [
    path('register/', RegisterApi.as_view()),
]