from django.contrib import admin
from .models import Product
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['title','price','category']


admin.site.register(Product, AdminProduct)