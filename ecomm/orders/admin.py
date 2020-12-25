from django.contrib import admin
from .models import Order
# Register your models here.
class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','datetime']

admin.site.register(Order,AdminOrder)
