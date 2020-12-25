from django.db import models
from categories.models import Categories
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Categories ,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default="Hey its Cool")
    images =  models.ImageField(upload_to="products_images/")

    def __str__(self):
        return self.title


    @staticmethod
    def get_product_by_ids(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_category(category_id):
        if category_id is not None:
            return Product.objects.filter(category= category_id)
        else:
            Product.get_products()

