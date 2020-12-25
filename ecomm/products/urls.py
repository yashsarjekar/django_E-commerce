from django.contrib import admin
from django.urls import path
from .views import Index,Cart
urlpatterns = [
    path('', Index.as_view(),name="home_page"),
    path('cart',Cart.as_view(),name="cart")
]
