"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from customers.views import Login,logout
from orders.views import Checkout,Orders
from . import settings
from products.middleware.auth import auth_middleware 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('register', include('customers.urls')),
    path('login',Login.as_view(),name='login'),
    path('logout',logout),
    path('checkout',auth_middleware(Checkout.as_view())),
    path('orders',auth_middleware(Orders.as_view()))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
