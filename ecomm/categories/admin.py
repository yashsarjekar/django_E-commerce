from django.contrib import admin
from .models import Categories
# Register your models here.


class AdminCategories(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Categories,AdminCategories)
