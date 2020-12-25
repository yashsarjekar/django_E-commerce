from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @staticmethod
    def get_categories():
        return Categories.objects.all()