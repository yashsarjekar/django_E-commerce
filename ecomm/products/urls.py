from django.contrib import admin
from django.urls import path
from .views import Index,Cart,Detail
urlpatterns = [
    path('', Index.as_view(),name="home_page"),
    path('cart',Cart.as_view(),name="cart"),
    path('details',Detail.as_view()),
]
