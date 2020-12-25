from django.contrib import admin
from .models import Customer
# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Customer, AdminCustomer)