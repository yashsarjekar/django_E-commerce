from django.contrib import admin
from django.urls import path
from .views import Register
urlpatterns = [
    path('', Register.as_view()),
]
